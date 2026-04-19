
from math import log2

def countHA_Adder(n):
    return 1+(2*(n-1))

def countHA_BAT(k):
    FL = 2 * k
    klog = (int)(log2(k))
    Total = 0

    for i in range(klog-1):
        (i+1)
