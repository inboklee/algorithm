import random

def quicksort(L):
    if (len(L) == 1) or (len(L) == 0):
        return L
    
    pivot = L[0]
    left = []
    right = []
    for x in L[1:]:
        if (x < pivot):
            left.append(x)
        else:
            right.append(x)
    return quicksort(left) + [pivot] + quicksort(right)
    
def randomizedquicksort(L):
        if (len(L) == 1) or (len(L) == 0):
                return L

        pivot = int(random.random() * len(L))
        left = []
        right = []
        for x in L[:pivot]+L[pivot+1:]:
                if (x < L[pivot]):
                        left.append(x)
                else:
                        right.append(x)
        return randomizedquicksort(left) + [L[pivot]] + randomizedquicksort(right)
        
