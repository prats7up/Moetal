from sympy import *
from sympy.physics.vector import ReferenceFrame

k = symbols('k')

R= ReferenceFrame('R')
from sympy.physics.vector import curl

F = sin(k * R[2])*R.x + cos(k * R[2])*R.y
print (curl(F,R))