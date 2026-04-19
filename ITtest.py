
from InfoTheory import *

Dict = ['A','B']
P = [0.9, 0.1]


a = genArray(P, 10)
print(a)
s = genString(Dict, P, 10)
print(s)
print(getEntropy(P))