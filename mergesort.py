def merge(A, B):
    C = []
    if (len(A) == 0):
        C = list(B)
        return C
    if (len(B) == 0):
        C = list(A)
        return C
    if (A[0] < B[0]):
        return [A[0]] + merge(A[1:], B)
    else:
        return [B[0]] + merge(A, B[1:])

def mergesort(L):
    if (len(L) == 1):
        return L
    return merge(mergesort(L[:len(L)/2]), mergesort(L[len(L)/2:]))
    
