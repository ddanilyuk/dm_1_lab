def func_1(A, B, C):
    x = set((A & (A - (A - B)) | C))
    return x


def func_3(A, B):
    x = set(A & B)
    return x


def func_2(A, B):
    A = list(A)
    B = list(B)
    C =[]
    for j in range(len(A)):
        for i in range(len(B)):
            if A[j] == B[i]:
                C.append(A[j])

    return set(C)
