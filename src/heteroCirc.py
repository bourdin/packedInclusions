import numpy as np
from numpy.random import random
from math import pi
import argparse
import os

# np.random.seed(123456789)

#Parsing des arguments
parser = argparse.ArgumentParser(description="")
parser.add_argument('--d', type=float, help="Target density of inclusions.", default = 0.4)
# parser.add_argument('--phi', type=float, help="Rotation angle of the sample", default = 0.)
parser.add_argument('-n','--numRotations', type=int, help="number of rotations of the microstructure inside the sample", default = 1)
parser.add_argument('--prefix',type=str,help ="meshes prefix", default="mesh")
parser.add_argument('--R', type=float, help="Radius of inclusions.", default = 0.1)
parser.add_argument('--var', type=float, help="Radius of inclusions.", default = 0.1)
parser.add_argument('--SampleRadius', type=float, help="Radius all the sample.", default = 2.)
parser.add_argument('--createAttempts', type=int, help="Number of attempts at creating a circle", default = 500)
parser.add_argument('--overwrite', type=bool, help='Rewrite the circles.geo file.', default=True)
parser.add_argument('--seed',type=int, help='Random generator seed',default=None)
args = parser.parse_args()
d, nRot, R, var, SampleRadius, createCircleAttempts, seed = args.d, args.numRotations, args.R, args.var, args.SampleRadius, args.createAttempts, args.seed
if seed:
    np.random.seed(seed)
# print(args)

minRadius, maxRadius = R*(1-var), R*(1+var)
BIGDISKRADIUS = SampleRadius + maxRadius
nb_circle = int(np.floor(d*BIGDISKRADIUS**2/R**2))
print(f'num inclusions: {nb_circle}')

circles = []

def createCircle():
    circleIsSafe = False
    for tries in range(createCircleAttempts):
        theta, module = 2*pi*random(), SampleRadius*random()**0.5
        x,y,R = module*np.cos(theta),module*np.sin(theta), minRadius
        if not isColliding(x,y,R):
            circleIsSafe = True 
            break
    
    if not circleIsSafe:
        return 0

    for radiusSize in np.arange(minRadius, maxRadius, 0.005):
        R = radiusSize
        if isColliding(x,y,R):
            R -= 0.01
            break
    
    circles.append(np.array([x,y,R]))


def isColliding(x,y,R):

    for circ in circles:
        xi,yi,Ri = circ
        a = R + Ri; X = x-xi; Y = y-yi

        if a**2 >= X**2 + Y**2:
            return True

    return False

for _ in range(nb_circle):
    createCircle()
circles = np.array(circles)

# #Rotation des cercles
# for circ in circles:
#     xi, yi = circ[0], circ[1]
#     circ[0], circ[1] = np.cos(phi)*xi - np.sin(phi)*yi, np.sin(phi)*xi + np.cos(phi)*yi

print("target density : ", d)
print("actual density : ", np.sum((circles[:,2])**2)/BIGDISKRADIUS**2)

#plot for checking
import matplotlib.pyplot as plt
fig, ax= plt.subplots(1,1)
ax.set_xlim([-3,3]); ax.set_ylim([-3,3])
U = np.linspace(0,2*pi, 100)
ax.plot(BIGDISKRADIUS*np.cos(U), BIGDISKRADIUS*np.sin(U), color = "black")
ax.hlines( BIGDISKRADIUS, -3, 0, color = "black", linestyle='dashed')
ax.hlines(-BIGDISKRADIUS, -3, 0, color = "black", linestyle='dashed')

ax.set_aspect("equal", adjustable="box")
ax.set_yticks([-BIGDISKRADIUS, 0, +BIGDISKRADIUS]);
ax.set_yticklabels([str(-BIGDISKRADIUS), "0", str(BIGDISKRADIUS)])
ax.set_xticks([0])

# circlesOnAxis = circles[np.abs(circles[:,1])<=2*R]
# Ys = circlesOnAxis[:,1]/R
# print(Ys.std())

for circ in circles:
    ax.plot(circ[0] + circ[2]*np.cos(U), circ[1] + circ[2]*np.sin(U), color = "black", linewidth = 1)
plt.savefig(f"figures/{args.prefix}-000.pdf")


if args.overwrite:
    for rot in range(nRot):   
        phi = 2.*np.pi/nRot*rot
        with open("circles.geo", 'w') as geo:
            geo.write("CircTags = {}; \n")
            for circ in circles:
                xi, yi = circ[0], circ[1]
                circ[0], circ[1] = np.cos(phi)*xi - np.sin(phi)*yi, np.sin(phi)*xi + np.cos(phi)*yi
                geo.write(f"i = news;\n Circle(i) = {{ {circ[0]}, {circ[1]}, 0., {circ[2]} }}; \n Curve Loop (i) = i; Surface(i) = i; CircTags += i; \n")
        os.system(f"gmsh -2 -o meshes/{args.prefix}-{rot:03d}.msh heteroCirc.geo")