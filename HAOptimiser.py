import math

HAtable = [0, 0, 1, 2, 4, 5, 7, 8, 11, 12, 14, 18, 19, 21, 22, 23, 26, 28, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129]

def l2fi(x):
    a = math.log(x,2)
    b = math.floor(a)
    c = b + 1
    return c

def pyramid_array(b: int, h: int) -> list:

    if not (isinstance(b, int) and isinstance(h, int)):
        raise TypeError("b and h must be integers")
    if b <= 0 or h <= 0:
        raise ValueError("b and h must be positive")
    if h > (b + 1) // 2:   # ceil(b/2) == (b+1)//2 for integers
        print(b)
        print(h)
        raise ValueError("Invalid pyramid: height h cannot exceed ceil(b/2)")

    ascending = list(range(1, h + 1))
    descending = list(range(h - 1, 0, -1))
    plateau_size = b - (len(ascending) + len(descending))  # >= 0 because of the check

    return ascending + [h] * plateau_size + descending

def apply_l2fi_and_propagate(arr):
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    n = len(arr)
    out = arr.copy()
    for i in range(n):
        v = out[i]
        if not (isinstance(v, int) and v > 0):
            raise ValueError("all array values must be positive integers")
        l2fi = v.bit_length()   # floor(log2(v)) + 1
        k = l2fi - 1
        # increment next k positions (safe-bounded)
        end = min(n, i + k + 1)  # end is exclusive
        for j in range(i + 1, end):
            out[j] += 1
    return out


def modified_pyramid(b: int, h: int) -> list:
    arr = pyramid_array(b, h)
    returnarr = apply_l2fi_and_propagate(arr)
    ##print(returnarr)
    return returnarr

def PAHAcount(b,h):
    arr = modified_pyramid(b,h)
    total = 0
    for i in range(b):
        HammingAdder = arr[i]
        total += HAtable[HammingAdder]
    return total

def HACount(a,b):
    n = a*b
    c = l2fi(b)
    d = l2fi(a)

    WScount = a*HAtable[b]
    CScount = c*HAtable[a]
    PAcount = PAHAcount((d+c-1),min(c,d))

    return WScount + CScount + PAcount


def factor_pairs(n: int) -> list[tuple[int, int]]:

    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    pairs = []
    for a in range(2, int(n**0.5) + 1):
        if n % a == 0:
            b = n // a
            if b >= 2:
                pairs.append((a, b))
                if a != b:
                    pairs.append((b, a))
    return pairs


print(HACount(32,3))


def tr_MHAcount(n):
    return (2*n*n) - (3*n)

def my_MHAcount(n):
    return PAHAcount((2*n)-1,n)

