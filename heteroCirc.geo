// Gmsh project created on Thu Apr 25 15:47:00 2024
SetFactory("OpenCASCADE");

// Définition des paramètres
L = 2.6;
epsilon = 0.001; //Crack maximum width
Rreel = 2;
var = 0.1;
fissure_init = -Rreel*(1 + var*1.5); //Initial crack tip
BigRadius = Rreel*(1+2*var);


lc1 = 0.005; //Finer mesh size
// lc2 = 0.02;  //Coarse mesh size
// lc1 = 0.01; //Finer mesh size
lc1 = 0.0075;
lc2 = 0.05;  //Coarse mesh size

DL = L;


//Domaine réel
Point(0) = {0,0,0};
Point(1) = {-(DL + L/2), -(DL + L/2), 0};
Point(2) = { (DL + L/2), -(DL + L/2), 0};
Point(3) = { (DL + L/2),  (DL + L/2), 0};
Point(4) = {-(DL + L/2),  (DL + L/2), 0};
Point(5) = {-(DL + L/2),  epsilon/2, 0};
Point(6) = {fissure_init, 0, 0};
Point(7) = {-(DL + L/2), -epsilon/2, 0};

A = 0.5*epsilon/(fissure_init + L/2 + DL);
discriminant = BigRadius^2*(1+A^2) - A^2*fissure_init^2;
x89 = (fissure_init*A^2 - Sqrt(discriminant))/(1+A^2);
y89 = A*(x89 - fissure_init);

Point(8) = {x89,-y89, 0};
Point(9) = {x89, y89, 0};



Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,5};
Line(5) = {5,8}; Line(55) = {8,6};
Line(66) = {6,9}; Line(6) = {9,7};
Line(7) = {7,1};
phi = Atan(y89/x89);
Circle(8) = {0,0,0, BigRadius, -Pi+phi, Pi-phi};


//Matériau 2
Include "circles.geo";
Physical Surface(2) = CircTags[];

//Matériau 1
Line Loop(1) = {-8,55,66};
Surface(1) = {1};
Physical Surface(11) = {1};
Physical Surface(1) = BooleanDifference {Physical Surface{11};} {Physical Surface{2};};
Delete{Physical Surface{11};}

//Matériau 3 (entourant)
ind = news;
Line Loop(0) = {1, 2, 3, 4, 5,-8, 6, 7};
Plane Surface(ind) = {0};
Physical Surface(3) = {ind};


//Conditions de bord
Physical Point(500) = {6};
Physical Line(300) = {5,6,55,66};
Physical Line(200) = {1,2,3,4,7};

//Maillage
	Field[1] = Ball;
	Field[1].Radius = BigRadius;
	Field[1].VIn = lc1;         
	Field[1].VOut = lc2;      
	Field[1].Thickness = 0.2; 

	Field[2] = Min;
	Field[2].FieldsList = {1};
	Background Field = 2;

Mesh 2;Coherence Mesh;
