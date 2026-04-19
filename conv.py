import MatrixLibrary as ML


x1 = [1, 2, 3]
x2 = [1, 2, 3]


def convolve(x,y):
    xlen = len(x)
    ylen = len(y)
    y = [0]*(xlen+ylen-1)
    for i in range(xlen):
        for j in range(ylen):
            y[i+j] += x1[i]*x2[j]
    return y


def linearconvolution(x,y):
    xlen = len(x)
    ylen = len(y)
    A = ML.genLinearKernelMatrix(x, xlen+ylen-1)
    A = ML.transpose(A)
    B = ML.vectorise(y)
    C = ML.product(A,B)
    z = ML.unvectorise(C)
    return z


def circularconvolution(a,b):
    alen = len(a)
    blen = len(b)

    if (alen > blen):
        x = a
        y = b
        d = alen-blen
    else:
        x = b
        y = a
        d = blen-alen

    y = y + [0] * d
    A = ML.genCircularKernelMatrix(x)
    B = ML.vectorise(y)
    C = ML.product(A,B)
    z = ML.unvectorise(C)
    return z


y = convolve(x1, x2)
print(y)

a = linearconvolution(x1, x2)
print(a)

b = circularconvolution(x1, x2)
print(b)

