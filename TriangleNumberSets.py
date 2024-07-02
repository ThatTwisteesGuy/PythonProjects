import time
from math import sqrt
from pynput.keyboard import Key, Controller
keyboard = Controller()

def invTriangle(x):
    return (int)((-1+sqrt(1+8*x))/2)

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
                    tuple = (invTriangle(tnums[i]), invTriangle(tnums[j]), invTriangle(tnums[k]))
                    perms.append(tuple)
    return perms

solutions = genSolutions(3066)
print(solutions)

time.sleep(5)
for i in range(len(solutions)):
    keyboard.type(str(solutions[i]))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)