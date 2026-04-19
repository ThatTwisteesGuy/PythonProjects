from math import log2, floor
import numpy as np
import heapq
from itertools import count
import itertools
import heapq
from collections import Counter


def checksum1(P):
    total = np.sum(P)
    if not np.isclose(total, 1.0):
        raise ValueError("Probabilities must sum to 1.")


def entropy(P):
    pdf = np.array(P)
    mask = pdf > 0
    return -np.sum(pdf[mask] * np.log2(pdf[mask]))


def genArray(D, L):
    Dist = np.array(D)
    pdf = Dist/Dist.sum()
    Array = np.random.choice(len(pdf), size=L, p=pdf)
    return Array


def genLVector(d):
    return [len(d[i]) for i in sorted(d.keys())]


def num_to_char(indices, D):
    Dict = np.array(D)
    return ''.join(Dict[indices])


def char_to_num(message, Dict):
    Dict = np.array(Dict)
    return np.where(Dict[:, None] == np.array(list(message)))[0]


def freqTable(Array):
    Array = np.array(Array, dtype=int)
    F = np.zeros(Array.max() + 1, dtype=int)
    for x in Array:
        F[x] += 1
    return F


def PDF(Array):
    F = freqTable(Array)
    PDF = np.array(F)/len(Array)
    return PDF


def encode_indices(Message, Symbols):

    Message = list(Message)  # ensure it's mutable
    code = []

    # maximum length of any symbol sequence
    maxLen = max(len(s) for s in Symbols)

    while len(Message) > 0:
        n = min(len(Message), maxLen)
        matched = False

        while n > 0:
            subMessage = Message[:n]

            # look for subMessage in Symbols
            for idx, symbol in enumerate(Symbols):
                if subMessage == symbol:
                    code.append(idx)
                    Message = Message[n:]  # remove matched part
                    matched = True
                    break

            if matched:
                break
            else:
                n -= 1

        if not matched:
            raise ValueError(f"Message not encodable at remaining sequence: {Message}")

    return code


def decode_indices(code, Symbols):
    message = []

    for idx in code:
        if idx < 0 or idx >= len(Symbols):
            raise ValueError(f"Invalid code index: {idx}")
        message.extend(Symbols[idx])  # append the symbol sequence corresponding to this index

    return message


def extended_probabilities(probs, m):
    if m == 1:
        return probs.copy()  # base case

    shorter = extended_probabilities(probs, m - 1)
    result = []

    for p in probs:
        for s in shorter:
            result.append(p * s)

    return result


def huffman_encoder(p):

    counter = count()  # tie-breaker to avoid comparing lists
    heap = [[prob, next(counter), i] for i, prob in enumerate(p)]
    heapq.heapify(heap)

    # Build Huffman tree
    while len(heap) > 1:
        prob1, _, sym1 = heapq.heappop(heap)
        prob2, _, sym2 = heapq.heappop(heap)
        # Merge nodes; sym1 and sym2 can be int or list
        heapq.heappush(heap, [prob1 + prob2, next(counter), [sym1, sym2]])

    # Generate codes
    codes = {}

    def generate_codes(node, code=""):
        if isinstance(node, int):
            codes[node] = code
        elif isinstance(node, list):
            generate_codes(node[0], code + "1")
            generate_codes(node[1], code + "0")

    root = heap[0][2]  # root node
    generate_codes(root)

    return dict(sorted(codes.items()))


def genString(Dict, Dist, Length):
    idx_array = genArray(Dist, Length)
    char_list = num_to_char(idx_array, Dict)
    return ''.join(char_list)
