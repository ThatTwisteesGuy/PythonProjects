from math import acos
from math import sqrt

def identity(n):
    I = generate(n, n)
    for x in range(n):
        I[x][x] = 1
    return I


def display(A):
    for i in range(len(A)):
        print("|", end = " ")
        for j in range(len(A[i])):
            print(A[i][j], end = " ")
        print("|")
    print("")


def populate(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            (A[i][j]) = float(input("Populate Cell: "))


def generate(m, n):
    return [[0 for j in range(n)] for i in range(m)]


def product(A, B):
    rA = len(A)
    cA = len(A[0])

    rB = len(B)
    cB = len(B[0])

    if cA != rB:
        print("Invalid Matrices")
        return None

    C = generate(rA, cB)

    for i in range(rA):
        for j in range(cB):
            for k in range(cA):
                C[i][j] += A[i][k] * B[k][j]
    return C


def copy(A):
    C = generate(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j]
    return C


def transpose(A):
    X = generate(len(A[0]), len(A))
    for i in range(len(X)):
        for j in range(len(X[0])):
            X[i][j] = A[j][i]
    return X


def flip(A):
    X = generate(len(A), len(A[0]))
    for i in range(int(len(A)/2)+1):
        X[i] = A[len(A)-1-i]
        X[len(A) - 1 - i] = A[i]
    return X


def mirror(A):
    X = generate(len(A), len(A[0]))
    for i in range(len(A[0])):
        for j in range(len(A)):
            X[i][j] = A[i][len(A[0])-1-j]
    return X


def rotate(A):

    X = transpose(A)
    Y = mirror(X)
    return Y


def roundMatrix(A, n):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = round((A[i][j]), n)
    return A


def isOrthogonal(A):
    idM = identity(len(A))
    idC = product(A, transpose(A))

    roundMatrix(idC, 6)
    if idC == idM:
        return True
    else:
        return False


def isSymmetric(A):
    for i in range(len(A)-1):
        for j in range(i+1,len(A[i])):
            if (A[i][j] != A[j][i]):
                return False
    return True


def determinant(A):
    if len(A) == 1:
        return A[0][0]

    elif len(A) == 2:
        return (A[0][0]) * (A[1][1]) - (A[1][0]) * (A[0][1])

    else:
        total = 0
        for i in range(len(A)):
            total += A[0][i] * genCofactor(A, 0, i)
        return total


def genCofactor(A, x, y):
    s = len(A)-1
    tA = copy(A)
    del (tA[x])
    for i in range(s):
        del(tA[i][y])
    CF = determinant(tA)*(1+(-2*((x+y)%2)))
    return CF

def divide(A, x):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = (A[i][j]) / x
    return A

def multiply(A, x):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = (A[i][j]) * x
    return A

def cofactorMatrix(A):
    X = generate(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[i])):
            (X[i][j]) = genCofactor(A, i, j)
    return X

def swapRows(A, x1, x2):
    X = copy(A)
    X[x1] = A[x2]
    X[x2] = A[x1]
    return X

def inverse(A):
    det = determinant(A)
    if det == 0:
        return None
    inverse = divide(transpose(cofactorMatrix(A)), det)
    return inverse

def solveSystem(A, v):
    Ainv = inverse(A)
    if Ainv is None:
        print("System has inf solutions")
        return None
    r = product(Ainv,v)
    if r is None:
        print("System is Incompatible")
        return None
    else:
        return r


def isVector(v):
    if len(v[0]) == 1:
        return True
    else:
        return False


def dotProduct(v1, v2):
    if (isVector(v1) == False) or (isVector(v2) == False):
        print("Not a Vector!")
        return None
    if len(v1) != len(v2):
        print("Mismatched Vectors!")
        return None
    sum = 0
    for i in range(len(v1)):
        sum += (v1[i][0])*(v2[i][0])
    return sum


def modulus(v):
    l = len(v)
    if isVector(v) == False:
        print("Not a Vector!")
        return None
    sum = 0
    for i in range(l):
        sum += (v[i][0])*(v[i][0])
    mod = sqrt(sum)
    return mod


def angleBetweenVectors(v1 , v2):
    if (isVector(v1) == False) or (isVector(v2) == False):
        print("Not a Vector!")
        return None
    value = (dotProduct(v1,v2)/(modulus(v1)*modulus(v2)))
    if value > 1:
        value = 1
    elif value < -1:
        value = -1
    return acos(value)

