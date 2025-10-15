import InfoTheory
import InfoTheory as IT
from math import pow

n = 4
cs = int(pow(2,n))

P = [15/16, 1/16]
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
                address = f"{j:04b}"  # n-bit binary address
                code += "0" + address

    return code


def decode_bits(bits: str) -> str:
    decoded = ""
    current_chunk = None
    i = 0

    while i < len(bits):
        if bits[i] == "1":
            # If not the first chunk, store previous one
            if current_chunk is not None:
                decoded += "".join(current_chunk)
            # Start new chunk of 16 As
            current_chunk = ["A"] * 16
            i += 1

        elif bits[i] == "0":
            # Read next 4 bits for the address
            address_bits = bits[i+1:i+5]
            address = int(address_bits, 2)
            # Modify that position to 'B'
            current_chunk[address] = "B"
            i += 5  # Move past '0XXXX'

        else:
            raise ValueError(f"Unexpected bit '{bits[i]}' at position {i}")

    # Add last chunk
    if current_chunk is not None:
        decoded += "".join(current_chunk)

    return decoded

def binary_to_int(binary_str: str) -> int:
    """Convert a binary string to integer."""
    return int(binary_str, 2)

def int_to_bin(n: int) -> str:
    return format(n & 0b11111, '05b')


def encode(s):
    code = ""
    last_index = -1

    length = int(len(s)/16)

    for i in range(length):
        chunk = s[0:16]
        b_indexes = [i for i, c in enumerate(chunk) if c == 'B']
        if b_indexes:
            if (b_indexes[0] > last_index > -1):
                code += '1'
            last_index = b_indexes[-1]
            for index in b_indexes:
                address = int_to_bin(index)
                code += address
        else:
            code += '1'
        s = s[16:]
    return code



def decode(bitstream):

    s = "AAAAAAAAAAAAAAAA"
    current_chunk = ""+s
    message = ""
    length = len(bitstream)
    last_index = -1
    current_index = -1
    iters_since_index = 0

    while length > 0:
        if (bitstream[0] == '1'):
            message += current_chunk
            bitstream = bitstream[1:]
            current_chunk = ""+s
            length = len(bitstream)
            iters_since_index += 1
        elif (bitstream[0] == '0'):
            iters_since_index = 0
            address = bitstream[1:5]
            current_index = binary_to_int(address)
            bitstream = bitstream[5:]
            if (-1 < current_index <= last_index):
                message += current_chunk
                current_chunk = ""+s
            current_chunk = current_chunk[:current_index] +'B'+ current_chunk[current_index+1:]
            last_index = current_index
            length = len(bitstream)
            if (length == 0):
                message += current_chunk
    if (iters_since_index >= 1):
        message += current_chunk
    return message

myString = InfoTheory.genString(Dict, P, cs*100000)

'''
print("Raw Data:")
print(myString)

print("Codes:")


print(myCode1)


print(myCode2)

print("Decoded Strings:")

decodedString1 = decode_bits(myCode1)
print(decodedString1)


print(decodedString2)
'''
myCode1 = encode_string(myString, cs)
myCode2 = encode(myString)
decodedString2 = decode(myCode2)
if (decodedString2 == myString):
    print("Yippee!!")
else:
    print("Shit!")


print("Efficiencies:")


A = len(myCode1)/len(myString)
B = len(myCode2)/len(myString)

H = IT.getEntropy(P)
efficiency1 = H/A
efficiency2 = H/B


print(efficiency1)
print(efficiency2)