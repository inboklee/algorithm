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

def BFS(G, start):
    isMarked = [False for _ in xrange(len(G))]
    isinQueue = [False for _ in xrange(len(G))]
    Q = []
    Q.insert(0, start)
    isinQueue[start] = True
    while (len(Q) > 0):
            current = Q.pop()
            print current
            isMarked[current] = True
            for e in G[current]:
                if (isMarked[e] == False) and (isinQueue[e] == False):
                    Q.insert(0, e)
                    isinQueue[e] = True
    return

G = [[], [2,6,8], [1,3,6], [2,4], [3,5], [2,3], [1,2,7,8], [6], [1,6]]

DFS(G, 1)
BFS(G, 1)
