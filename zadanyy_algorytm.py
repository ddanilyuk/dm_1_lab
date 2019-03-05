def func_1_full(A, B, C):
    # y = set(((A - B) | (B & A)) - (C | B))
    x = set(difference(union(difference(A, B), crossing(B, A)), union(C, B)))
    return x


def func_1_small(A, B, C):
    # y = set(A - (C | B))
    x = set(difference(A, union(C, B)))
    return x


def func_2_my(A, B):
    A = list(A)
    B = list(B)
    C = []
    for i in A:
        q = 0
        for j in B:
            if i == j:
                q = 1
        if q == 0:
            C.append(i)
    return set(C)


def func_2_python(A, B):
    x = set(A & B)
    return x


###################
# other functions #
###################
def crossing(A, B):
    A = list(A)
    B = list(B)
    C = []
    for j in range(len(A)):
        for i in range(len(B)):
            if A[j] == B[i]:
                C.append(A[j])
    return set(C)


def difference(A, B):
    A = list(A)
    B = list(B)
    C = []
    for i in A:
        q = 0
        for j in B:
            if i == j:
                q = 1
        if q == 0:
            C.append(i)
    return C


def union(a, b):
    a = list(a)
    b = list(b)
    c = b.copy()
    for i in a:
        q = 0
        for j in b:
            if i == j:
                q = 1
        if q == 0:
            c.append(i)
    return c


def sym_dif(a, b):
    a = list(a)
    b = list(b)
    c = []
    for i in range(len(a)):
        if (a[i] not in b):
            c.append(a[i])
    for j in range(len(b)):
        if (b[j] not in a):
            c.append(b[j])
    return (c)


def no_set(A, U):
    U = list(U)
    A = list(A)
    C = []
    for i in U:
        q = 0
        for j in A:
            if i == j:
                q = 1
        if q == 0:
            C.append(i)
    return set(C)


def notX(X, U):
    nX = set(U)
    for elem in X:
        if elem in nX:
            nX.remove(elem)
    return nX
