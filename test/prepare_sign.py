

def recurse(pData, pList):
    lStack = [pData]
    while len(lStack) is not 0:
        lObj = lStack.pop()
        if type(lObj) is dict:
            for lValue in sorted(lObj.items()):
                lStack.append(lValue)
        elif type(lObj) is list or type(lObj) is tuple:
            for lElem in sorted(lObj):
                lStack.append(lElem)
        else:
            pList.append(str(lObj))


def canonicalize(pData):
    lElemList = []
    recurse(pData, lElemList)

    return '\n'.join(lElemList)



