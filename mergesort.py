def merge(A, B):
    if (len(A) == 0):
        return B
    if (len(B) == 0):
        return A
    if (A[0] < B[0]):
        return [A[0]] + merge(A[1:], B)
    else:
        return [B[0]] + merge(A, B[1:])

def mergesort(L):
    if (len(L) == 1):
        return L
    return merge(mergesort(L[:len(L)/2]), mergesort(L[len(L)/2:]))
    
