def HW(s: str) -> str:
    # Step 1: count the number of 1s
    ones_count = s.count("1")

    # Step 2: find the maximum possible count = length of string
    max_count = len(s)

    # Step 3: find how many bits are needed to represent max_count
    bits_needed = max_count.bit_length()

    # Step 4: convert actual count to binary string
    result = bin(ones_count)[2:]  # strip '0b'

    # Step 5: pad with leading zeros
    return result.zfill(bits_needed)

def HA(a: str, b: str) -> str:
    """
    Half Adder: takes 2 inputs ('0' or '1') and returns 2-bit string.
    First bit = carry, second bit = sum.
    """
    A, B = int(a), int(b)
    carry = A & B
    summ = A ^ B
    return f"{summ}{carry}"


def FA(a: str, b: str, cin: str) -> str:
    """
    Full Adder: takes 3 inputs ('0' or '1') and returns 2-bit string.
    First bit = carry, second bit = sum.
    """
    A, B, C = int(a), int(b), int(cin)
    summ = A ^ B ^ C
    carry = (A & B) | (B & C) | (A & C)
    return f"{summ}{carry}"

def H8(A: str) -> str:
    B = FA(A[0],A[1],A[2])
    C = FA(A[3],A[4],A[5])
    D = HA(A[6],A[7])

    E = FA(B[0], C[0], D[0]) ## Sum of Sums
    F = FA(B[1], C[1], D[1]) ## Sum of Carries

    G = HA(E[1], F[0])
    H = HA(G[1], F[1])

    I = E[0] + G[0] + H
    CircuitOutput = I[::-1]
    return CircuitOutput

def H5(A: str) -> str:
    B = FA(A[4], A[3], A[2])
    C = FA(B[0], A[1], A[0])
    D = HA(B[1], C[1])
    I = C[0] + D

    CircuitOutput = I[::-1]
    return CircuitOutput

def generate_binary_strings(n: int):
    for i in range(2**n):
        yield format(i, f'0{n}b')  # binary string with leading zeros

testPass = True
failedString = ""

for A in generate_binary_strings(5):
    VerifierOutput = HW(A)
    CircuitOutput = H5(A)
    if VerifierOutput != CircuitOutput:
        testPass = False
        failedString = A

if testPass == True:
    print("Test Passed!")
else:
    print("Test Failed")
    print(failedString)
