
import random

def generate_random_ints(n: int, min_val: int, max_val: int) -> list:

    return [random.randint(min_val, max_val) for _ in range(n)]

x = generate_random_ints(64, -32767, 32767)
print(x)