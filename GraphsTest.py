import random

n = 3

E = []
W = 0

for i in range(n):
    x = random.randint(1,10)
    E.append(x)
    W += x


z = 0

Wp = W/2

print(E)
print(W)
print(Wp)

print("The edge is:\n")

for i in range(len(E)):
    z += E[i]
    if z > Wp:
        print(i)
        break

