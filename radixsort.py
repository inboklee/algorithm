import math

def radixsort(L):
        temp = list(L)
        bucket = [[] for _ in xrange(10)]
        for x in xrange(int(math.log(max(L), 10))+1):
                bucket = [[] for _ in xrange(10)]
                for l in temp:
                        digit = (l % int(math.pow(10, x+1))) / int(math.pow(10,\
 x))
                        bucket[digit].append(l)
                temp = []
                for i in xrange(len(bucket)):
                        temp = temp + bucket[i]
                        bucket[i] = []
                print temp
        return temp
