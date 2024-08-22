import time
from math import sqrt
from pynput.keyboard import Key, Controller
keyboard = Controller()

def invTriangle(x):
    return (int)((-1+sqrt(1+8*x))/2)

def genSolutionsUnq(n):
    tnums = []
    i = 0
    temp = 0
    while True:
        if temp > n:
            break
        tnums.append(temp)
        i += 1
        temp += i
    combs = []
    size = len(tnums)
    for i in range(size):
        for j in range(i,size):
            for k in range(j,size):
                if (tnums[i] + tnums[j] + tnums[k]) == n:
                    tp = (invTriangle(tnums[k]), invTriangle(tnums[j]), invTriangle(tnums[i]))
                    combs.append(tp)
    return combs

def genSolutions(n):
    tnums = []
    i = 0
    temp = 0
    while True:
        if temp > n:
            break
        tnums.append(temp)
        i += 1
        temp += i
    perms = []
    size = len(tnums)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if (tnums[i] + tnums[j] + tnums[k]) == n:
                    tp = (invTriangle(tnums[k]), invTriangle(tnums[j]), invTriangle(tnums[i]))
                    perms.append(tp)
    return perms

n = 100

solutions = genSolutionsUnq(n)
print(solutions)


time.sleep(5)
#string = ("n = ")
#keyboard.type(string)
#keyboard.type(str(n))

time.sleep(0.1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
solutions = genSolutionsUnq(n)
keyboard.type(str(solutions))

time.sleep(0.1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
solutions = genSolutions(n)
keyboard.type(str(solutions))