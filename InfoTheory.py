from math import log2, floor
from random import choices


def checksum1(P):
    total = 0
    for i in range(len(P)):
        total += P[i]
    if abs(total - 1.0) > 1e-6:
        raise ValueError("Probabilities must sum to 1.")


def Entropy(P):
    checksum1(P)
    H = 0
    for i in range(len(P)):
        if P[i] != 0:
            H -= P[i] * log2(P[i])
    return H


def genString(Dict, P, Length):
    checksum1(P)

    if (len(Dict) != len(P)):
        raise ValueError("Dictionary and Probabilities Lists are not of Equal Length")

    result = choices(Dict, P, k=Length)
    return ''.join(result)


def denum(x, D):

    D.sort(reverse=True)
    size = len(D)

    A = [0] * size

    for i in range(size):
        A[i] = floor(x / D[i])
        x -= A[i]*D[i]

    return A


def freqTable(Message, Dict, ProbForm=False):

    Mlen = len(Message)
    Dlen = len(Dict)

    F = [0]*Dlen

    for c in Message:
        indexinDict = Dict.index(c)
        F[indexinDict] += 1

    if ProbForm == True:
        for i in range(Dlen):
            F[i] /= Mlen

    return F


myDict = ['A', 'B']
myString = "AAAAB"

freq = freqTable(myString, myDict, False)
print(freq)