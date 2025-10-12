import random
import math
import InfoTheory

oldDict = ['A', 'B']
newDict = ["A", "B", "C", "D"]
newDict = ["00", "01", "11", "10"]

p = [0.7, 0.3]
D = [7,3,1]

def encode(S):

    code = ""
    Acount = 0

    for c in S:
        if c == 'A':
            Acount += 1

        elif c == 'B':

            A = InfoTheory.denum(Acount, D)

            for i in range(1, len(A)):
                code += newDict[i] * A[i]
            code += newDict[0]
            Acount = 0

    A = InfoTheory.denum(Acount, D)

    for i in range(1, len(A)):
        code += newDict[i] * A[i]

    return code


myString = InfoTheory.genString(oldDict, p, 10000)

myCode = encode(myString)

dataL = len(myString)
dataC = len(myCode)


Lavg = dataC/dataL

entropy = InfoTheory.Entropy(p)

eff = entropy/Lavg

print(eff)

