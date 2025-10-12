
from MatrixLibrary import *
import random
import math

##for i in range(1, 200):
    ##print("finished:",i)
    ##for j in range(1, 200):
        ##for k in range(1, 200):

i = 1
j = 1
k = 1

x1 = i*i
x3 = j*j
x5 = k*k

x2 = 3*x5-x3-x1
x4 = x3+x5-x1
x6 = x1+x5-x3
x8 = x1+x3-x5

x7 = 2*x5 - x3
x9 = 2*x5 - x1

if (x2 > 0 and x4 > 0 and x6 > 0 and x8 > 0 and x7 > 0 and x9 > 0 and x1 != x3 and x1 != x5 and x3 != x5):
    print("magic square found")
    A = generate(3,3)
    A = [[x1,x2,x3],[x4,x5,x6],[x7,x8,x9]]
    display(A)