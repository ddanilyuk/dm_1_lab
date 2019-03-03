def notX(X, U):
    nX = set(U)
    for elem in X:
        if elem in nX:
            nX.remove(elem)
    return nX


def vyraz(A, B, C, U):
    x = set(((A & notX(B, U)) | (B & notX(A, U))) & (C | B) & C)
    return x


def vyraz_1(A, B, C, U):
    x = set((A & (A - (A - B)) | C))
    return x


def vyraz_2(A, B):
    x = set(A & B)
    return x
