#!/usr/bin/env python3
import sys

def parse(args=None):
    import argparse
    ### Get options from the command line
    parser = argparse.ArgumentParser(description='Plot energy evolution for VarFracQS.')
    parser.add_argument('inputfile',type=argparse.FileType('r'),nargs='?',help='Input file',default=sys.stdin)
    parser.add_argument('-o','--outputfile',help='output file',default=None)
    parser.add_argument("-m","--stepmin",type=int,help="first time step")
    parser.add_argument("-M","--stepmax",type=int,help="last time step")
    parser.add_argument("--size",type=float,nargs=2,default=None,help="Figure size")
    parser.add_argument("--title",default=None,help="Figure title")
    return parser.parse_args()

def main():
    import matplotlib
    import numpy as np
    options = parse()

    energies=np.loadtxt(options.inputfile)
      
    if options.stepmin == None:
      tmin = 0
    else:
      tmin = int(options.stepmin)
    if options.stepmax == None:
      tmax = energies.shape[0]
    else:
      tmax = int(options.stepmax)
    
    
    if options.outputfile != None:
      matplotlib.use('Agg')
      useTex=True
    else:
     useTex = False
    import matplotlib.pyplot as plt

    
    fig = plt.figure(figsize=options.size)
    
    ### plot
    plt.plot(energies[tmin:tmax,0],energies[tmin:tmax,1],'o',label=r'$J$')
    plt.grid()
    plt.legend(loc=0)
    plt.xlabel('t')
    plt.ylabel(r'RJ$')
    if options.title:
        plt.title(options.title)
    else:
        plt.title(r'$J$--integral vs. normalized time')
    #pymef90.setspines()

    ### export plot if needed
    if options.outputfile != None:
      fig.tight_layout(pad=0.1)
      plt.savefig(options.outputfile)
    else:
      plt.show()

if __name__ == "__main__":
        sys.exit(main())
