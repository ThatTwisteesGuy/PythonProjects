from math import pow
import InfoTheory as IT

P = [1/129, 64/129, 64/129]
H = IT.getEntropy(P)
print(H)

print(IT.getEntropy([4/16, 12/16]))