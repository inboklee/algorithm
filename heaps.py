ef fix_minheap_bottom(L, start, k):
        while (k > start):
                parent = int((k-1)/2)
                if (L[parent] > L[k]):
                        L[parent], L[k] = L[k], L[parent]
                else:
                        return 0
        return 0

def fix_minheap_top(L, start, end):
        if (start >= end):
                return 0
        left = start*2 + 1
        right = start*2 + 2
        if (left <= end) and (L[left] < L[start]):
                L[left], L[start] = L[start], L[left]
                fix_minheap_top(L, left, end)
        if (right <= end) and (L[right] < L[start]):
                L[right], L[start] = L[start], L[right]
                fix_minheap_top(L, right, end)
        return 0

def check_minheap(L):
        for k in xrange(1,len(L)):
                parent = int((k-1)/2)
                if (L[parent] > L[k]):
                        return False
        return True

def insertheap(L, x):
        L.append(x)
        fix_minheap_bottom(L, 0, len(L)-1)

def inc_buildheap(L):
        temp = []
        for x in L:
                insertheap(temp, x)
        return temp

def buildheap(L):
        if (len(L) == 1):
                return 0

        right = 2
        while (right < len(L)):
                right = right * 2 + 2
        right = (right - 2) / 2
        left = right / 2

        while (right >= 0):
                for x in xrange(left, right+1):
                        fix_minheap_top(L, x, len(L)-1)
                right = left - 1
                left = right/2
        return 0

def pop_head(L, last):
        L[last], L[0] = L[0], L[last]
        fix_minheap_top(L, 0, last-1)

def heapsort(L):
        last = len(L)-1
        while (last >= 0):
                pop_head(L, last)
                last = last - 1
                
