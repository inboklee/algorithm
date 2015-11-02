def DFS(G, start):
    isMarked = [False for _ in xrange(len(G))]

    recursiveDFS(G, isMarked, start)

def recursiveDFS(G, isMarked, start):
    if (isMarked[start] == True):
        return
    else:
        print start
        isMarked[start] = True
        for e in G[start]:
            recursiveDFS(G, isMarked, e)
        return
G = [[], [2,6,8], [1,3,6], [2,4], [3,5], [2,3], [1,2,7,8], [6], [1,6]]

DFS(G, 1)
