import math

def get_factors(n: int):
    factors = []
    for i in range(math.ceil(math.sqrt(n))):
        if n % (i + 1) == 0:
            factors.append((i + 1))
    return factors


def check_perfect(n: int):
    if n == 0 or n == 1:
        return False
    return sum(get_factors(n)) == n

print(get_factors(12))

for j in range(1000):
    if check_perfect(j):
        print(j)
