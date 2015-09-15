def selectk(L, k):
        if (len(L) == 1):
                return L[0]

        pivot = L[0]
        left = []
        right = []
        for x in L[1:]:
                if (x < pivot):
                        left.append(x)
                else:
                        right.append(x)
        if (len(left) ==  k-1):
                return pivot
        elif (len(left) >= k):
                return selectk(left, k)
        else:
                return selectk(right, k-(len(left)+1))
