def countingsort(L, n):
        n = n + 1
        C = [0 for _ in xrange(n)]
        for l in L:
                C[l] = C[l] + 1
        for i in xrange(1, n):
                C[i] = C[i-1] + C[i]

        C = [0] + C[:-1]
        for i in xrange(1, n):
                if (C[i] > C[i-1]):
                        for j in xrange(C[i-1], C[i]):
                                L[j] = i-1
        
        if (C[n-1] != len(L)):
                for j in xrange(C[n-1], len(L)):
                        L[j] = n-1
        return L
