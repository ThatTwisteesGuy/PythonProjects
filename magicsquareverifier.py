from MatrixLibrary import *
import random
import math

C = 1.6*pow(10, 50)
I = 1.2*pow(10, 50)
J = 1.4*pow(10, 50)
A = ((2*C*C)-(I*I))
B = ((2*C*C)-(J*J))
x2 = ((I*I)+(J*J)-(C*C))
x4 = ((I*I)-(J*J)+(C*C))
x6 = (-(I*I)+(J*J)+(C*C))
x8 = (-(I*I)-(J*J)+3*(C*C))


X = generate(3,3)
X = [[A, x2, B],[x4, C*C, x6],[J*J, x8, I*I]]

S1 = X[0][0] + X[0][1] + X[0][2]
S2 = X[1][0] + X[1][1] + X[1][2]
S3 = X[2][0] + X[2][1] + X[2][2]

S4 = X[0][0] + X[1][0] + X[2][0]
S5 = X[0][1] + X[1][1] + X[2][1]
S6 = X[0][2] + X[1][2] + X[2][2]

S7 = X[0][0] + X[1][1] + X[2][2]
S8 = X[2][0] + X[1][1] + X[0][2]


print("row 1: ",S1," row 2: ",S2," row 3: ",S3)
print("col 1: ",S4," col 2: ",S5," col 3: ",S6)
print("diag 1: ",S7," diag 2: ",S8)

print()
