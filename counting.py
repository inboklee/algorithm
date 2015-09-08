def brutecount(X):
    C = [0 for _ in xrange(len(X))]
    for i in xrange(len(X)):
        for j in xrange(i+1, len(X)):
            if (X[i] == X[j]):
                C[i] = C[i] + 1
    mostfrequent = 0
    for i in xrange(1, len(X)):
        if (C[i] > C[mostfrequent]):
            mostfrequent = i
    return X[mostfrequent]

def sortcount(X):
    C = sorted(X)
    current = C[0]
    count = 0
    maximal = C[0]
    maxcount = 0
    for x in C:
        if (x == current):
            count = count + 1
        else:
            if (count > maxcount):
                maxcount = count
                maximal = current 
            current = x
            count = 1
    return maximal
