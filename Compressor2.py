from InfoTheory import getEntropy, encode, genString, freqTable

P = [0.9, 0.1]
oldDict = ['A', 'B']
mySymbols = ["C", "D", "E", "F", "G", "H", "I", "J"]


myMessage = genString(oldDict, P, 29999) + 'B'

print(myMessage)

newDict = ["AAA", "AAB", "ABA", "BAA", "ABB", "BAB", "BBA", "BBB"]
binaryEncoding = ["1", "001", "010", "011", "00001", "00010", "00011", "00000"]

myCode = encode(myMessage, newDict, mySymbols)
myBinary = encode(myCode, mySymbols, binaryEncoding)

Lavg = len(myBinary)/len(myMessage)
H = getEntropy(P)

efficiency = H/Lavg

print(myBinary)

print(efficiency)

newDict = ["AAAAA","AAAAB","AAAB","AAB", "AB", "B"]
binaryEncoding = ["0","11111", "11110", "1110", "110", "10"]

myCode = encode(myMessage, newDict, mySymbols)
myBinary = encode(myCode, mySymbols, binaryEncoding)

Lavg = len(myBinary)/len(myMessage)
H = getEntropy(P)

efficiency = H/Lavg

print(efficiency)