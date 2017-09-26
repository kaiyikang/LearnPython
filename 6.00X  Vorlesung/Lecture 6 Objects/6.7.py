def applyToEach(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])


testList = [1,-4,8,-9]

def f(l):
    print(abs(l)**2)
    return

applyToEach(testList,f)