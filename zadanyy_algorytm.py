def func_1(A, B, C):
    x = set((A & (A - (A - B)) | C))
    return x


def func_2(A, B):
    x = set(A & B)
    return x
