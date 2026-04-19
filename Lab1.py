import matplotlib.pyplot as plt
import numpy as np
import InfoTheory as it

def stem(x):
    plt.stem(x)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Stem Plot')
    plt.show()

def plot(x, y):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Line Graph')
    plt.show()

p0 = [1/127]*127
L = 10000
M = it.genArray(p0, L)
F = it.freqTable(M)
PDF = it.PDF(M)
print(M)

H_tr = it.entropy(p0)
H_exp = it.entropy(PDF)

# print(H_tr)
# print(H_exp)

# stem(F)
# stem(PDF)

Entropies = []
p_space = np.linspace(0, 1, 101)
for x in p_space:
    p = [x, 1-x]
    H = it.entropy(p)
    Entropies.append(H)

plot(p_space, Entropies)
p1 = [0.3, 0.3, 0.2, 0.1, 0.05, 0.05]
hm = it.huffman_encoder(p1)
print(hm)
lv = it.genLVector(hm)
ACWL = np.dot(lv, p1)
print(ACWL)
H = it.entropy(p1)
print(H)
mu = H/ACWL
print(mu)

p1 = [0.9, 0.1]
hm = it.huffman_encoder(p1)
print(hm)
lv = it.genLVector(hm)
ACWL = np.dot(lv, p1)
print(ACWL)
H = it.entropy(p1)
print(H)
mu = H/ACWL
print(mu)


p1 = [0.9, 0.1]
m = 6
pext = it.extended_probabilities(p1, m)
hmext = it.huffman_encoder(pext)
print(hmext)
lv = it.genLVector(hmext)
ACWL = np.dot(lv, pext)
print(ACWL)
H = it.entropy(pext)
print(H)
mu = H/ACWL
print(mu)