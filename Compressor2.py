oldDict = ['A', 'B']
newDict = ["AAAA", "AA", "AB", "BA", "BB"]
mySymbols = ['C', 'D', 'E', 'F', 'G']


def encode(Message, Dict, Symbols):

    code = ""
    maxLen = 0
    for w in newDict:
        if len(w) > maxLen:
            maxLen = len(w)

    while(len(Message) <= maxLen):

        n = maxLen
        subMessage = Message[:n]

        if (subMessage not in newDict):
            n -= 1
            if (n == 0):
                print("Message not Encodable!")
                return
        else:
            index = newDict.index(subMessage)
            code += Symbols[index]

    return code

mycode = encode("AAAA", newDict, newDict)
print(mycode)