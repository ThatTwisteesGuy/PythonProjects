from math import pow
import InfoTheory as IT

P = [1/16, 15/16]
H = IT.getEntropy(P)
print(H)

print (H / (5.5/16))