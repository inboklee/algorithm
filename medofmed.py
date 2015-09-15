def medofmed(L):
        if (len(L) <= 5):
                return sorted(L)[len(L)/2]
        med = []
        current = 0
        while (current < len(L)):
                print current
                med.append(medofmed(L[current:current+5]))
                current = current + 5
        return medofmed(med)
