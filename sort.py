def bubblesort(L):
    result = list(L)
    for x in xrange(len(result)-1):
        for y in xrange(len(result)-x-1):
            if (result[y] > result[y+1]):
                result[y], result[y+1] = result[y+1], result[y]
    return result

def selectionsort(L):
    temp = list(L)
    result = []
    while (len(temp) > 0):
        m = min(temp)
        result.append(m)
        temp.remove(m)
    return result
