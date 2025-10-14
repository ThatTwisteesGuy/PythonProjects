import InfoTheory as IT
from math import pow

n = 5
cs = int(pow(2,n))

P = [31/32, 1/32]
Dict = ['A', 'B']

def encode_string(s: str, chunk_size) -> str:
    code = ""

    for i in range(0, len(s), chunk_size):
        chunk = s[i:i + chunk_size]

        # Step 1: Append "1" for each chunk
        code += "1"

        # Step 2: For each 'B' in this chunk, append 0 + address
        for j, char in enumerate(chunk):
            if char == 'B':
                address = f"{j:05b}"  # n-bit binary address
                code += "0" + address

    return code

myString = IT.genString(Dict, P, (cs*10000))

myCode = encode_string(myString, cs)

A = len(myCode)/len(myString)

H = IT.getEntropy(P)
efficiency = H/A

A = (n+2)/cs
theory = (H/A)
print("theoertical eff: ",theory)
print("actual eff: ",efficiency)