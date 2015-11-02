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
