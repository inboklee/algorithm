def selectk(L, k):
        if (len(L) == 1):
                return L[0]

        pivot = medofmed(L)
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

def medofmed(L):
        if (len(L) <= 5):
                return sorted(L)[len(L)/2]
        med = []
        current = 0
        while (current < len(L)):
                med.append(medofmed(L[current:current+5]))
                current = current + 5
        return selectk(med, int(len(med)/2))
