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
