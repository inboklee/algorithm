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

def FloydWarshall(G):
    n = len(G)
    dist = list(G)
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if (dist[i][j] > dist[i][k] + dist[k][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

