from collections import deque
from numpy.random import randint

from time import perf_counter


def get_time(f):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        ret = f(*args, **kwargs)
        end_time = perf_counter()
        total_time = round(end_time - start_time, 2)
        print("Time", total_time, "seconds")
        return ret

    return wrapper


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(row, col, m):
    rows = len(m)
    cols = len(m[0])
    arr = []
    for _ in range(rows):
        arr.append([None] * cols)
    arr[row][col] = 1
    queue = deque()
    queue.append((row, col))

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = (r + dr, c + dc)
            if 0 <= nr < rows and 0 <= nc < cols and arr[nr][nc] is None:
                arr[nr][nc] = arr[r][c] + 1
                if m[nr][nc] != 1:
                    queue.append((nr, nc))
    return arr


@get_time
def their_solution(m):
    rows = len(m)
    cols = len(m[0])
    src = bfs(0, 0, m)
    dest = bfs(rows - 1, cols - 1, m)
    res = 100000
    for i in range(rows):
        for j in range(cols):
            if src[i][j] and dest[i][j]:
                res = min(res, src[i][j] + dest[i][j] - 1)
                if res == rows + cols - 1:
                    return res
    return res


@get_time
def my_solution(graph):
    # breadth First Search beginning at 0,0
    # max one wall can be removed
    # nodes saved as [i,j,removed_wall]
    # removed_wall: bool -> whether a wall has been removed
    # may have [i,j,True] and [i,j,False] both in list but not a problem
    # only minor performance increase from removing this
    node = [0, 0, False]
    q = []
    v = []
    q.append([node, 1])
    while q:
        [node, dist] = q.pop(0)
        v.append(node)
        i, j, removed_wall = node
        if i == len(graph) - 1 and j == len(graph[-1]) - 1:
            return dist
        for d in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            newI = i + d[0]
            newJ = j + d[1]
            if 0 <= newI < len(graph) and 0 <= newJ < len(graph[newI]):
                if newI == len(graph) - 1 and newJ == len(graph[-1]) - 1:
                    return dist + 1
                if graph[newI][newJ] == 0:
                    newNode = [newI, newJ, removed_wall]
                    seen = False
                    if newNode in v:
                        seen = True
                    if removed_wall and [newI, newJ, False] in v:
                        seen = True
                    if not seen:
                        q.append([newNode, dist + 1])
                else:
                    if not removed_wall:
                        newNode = [newI, newJ, True]
                        if newNode not in v:
                            q.append([newNode, dist + 1])
    return 100000


@get_time
def solution(graph):
    # breadth First Search beginning at 0,0
    # max one wall can be removed
    # nodes saved as [i,j,removed_wall]
    # removed_wall: bool -> whether a wall has been removed
    # may have [i,j,True] and [i,j,False] both in list but not a problem
    # only minor performance increase from removing this
    node = [0, 0, False]
    q = []
    v = []
    q.append([node, 1])
    while q:
        [node, dist] = q.pop(0)
        v.append(node)
        i, j, removed_wall = node
        if i == len(graph) - 1 and j == len(graph[-1]) - 1:
            return dist
        for d in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            newI = i + d[0]
            newJ = j + d[1]
            if 0 <= newI < len(graph) and 0 <= newJ < len(graph[newI]):
                if newI == len(graph) - 1 and newJ == len(graph[-1]) - 1:
                    return dist + 1
                if graph[newI][newJ] == 0:
                    newNode = [newI, newJ, removed_wall]
                    seen = False
                    if newNode in v:
                        seen = True
                    if removed_wall and [newI, newJ, False] in v:
                        seen = True
                    if not seen:
                        q.append([newNode, dist + 1])
                        v.append(newNode)
                else:
                    if not removed_wall:
                        newNode = [newI, newJ, True]
                        if newNode not in v:
                            q.append([newNode, dist + 1])
                            v.append(newNode)
    return 100000


def run_tests():
    while True:
        for w in range(15, 21):
            for h in range(15, 21):
                graph = randint(0, 2, [w, h]).tolist()
                for f in [solution, my_solution, their_solution]:
                    f(graph)
                print()


run_tests()
