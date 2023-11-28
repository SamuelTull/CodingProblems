############################
# PLAN #####################
############################
# Search all paths
# at each iteration we have current viable paths q
# pick q with most T left
# we know we can NOT be gaining time infinitely so no problem getting stuck
# when path[-1] = E with B bunnies and T>=0
# set solution[B] = path (if not already found such solution)
# its okay to go slightly negative T, but at some point it will be impossible to get back in time
# crude method: add up all the negative values and if more negative than this is certainly impossible
# can also remove if reached N with B bunnies in less time previously
from collections import defaultdict


def negCycle(G):
    # negative cycle from (0,0)?
    # Using Bellman-Ford Algorithm
    N = len(G)
    d = [1e9 if i != 0 else 0 for i in range(N)]
    for _ in range(N - 1):
        for u in range(N):
            for v in range(N):
                d[v] = min(d[v], d[u] + G[u][v])
    for u in range(N):
        for v in range(N):
            if d[v] > d[u] + G[u][v]:
                return True
    return False


def sumNeg(G):
    s = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            s += min(G[i][j], 0)
    return s


def solution(G, T):
    N = len(G)
    if negCycle(G):
        return [x for x in range(N - 2)]

    maxNeg = sumNeg(G)

    end = N - 1

    q = []
    q.append([T, set(), [0]])
    # T, Bunnies, Path
    # T first so can sort list and pop

    v = {i: defaultdict(lambda: -1e9) for i in range(N)}
    v[0][str(set())] = 0

    sol = []

    while q:
        q.sort()
        [T, B, path] = q.pop()
        if T >= 0 and path[-1] == end:
            if list(B) not in sol:
                sol.append(list(B))
        for d in range(N):
            if d == path[-1]:
                # no benefit to staying in room
                # no -ve cycle means cost >=0 for no gain
                continue

            newT = T - G[path[-1]][d]
            if newT < maxNeg:  # cant get back in time
                continue
            if d == end or d in path:
                newB = B
            else:
                newB = B.union({d - 1})

            if v[d][str(newB)] >= newT:  # have reached d with B bunnies in less time
                continue

            v[d][str(newB)] = newT

            newP = path + [d]
            q.append([newT, newB, newP])
    for i in range(N):
        if sol[N - 1 - i] != set():
            return sol[N - 1 - i]


print(
    solution(
        [
            [0, 2, 2, 2, -1],
            [9, 0, 2, 2, -1],
            [9, 3, 0, 2, -1],
            [9, 3, 2, 0, -1],
            [9, 3, 2, 2, 0],
        ],
        1,
    )
)

print(
    solution(
        [
            [0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0],
        ],
        3,
    )
)
