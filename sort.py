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
        m = temp.pop(0)
        result.append(m)
        for i in range(1,len(result))[::-1]:
            if (result[i] < result[i-1]):
                result[i], result[i-1] = result[i-1], result[i]
    return result
