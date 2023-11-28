from collections import deque
from collections import Counter
import numpy as np


def findWords(self, board, words):
    root = Node()
    B = Counter(c for row in board for c in row)
    for word in words:
        if Counter(word) - B:
            continue
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.word = word

    Q = deque()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in root.children:
                Q.append(
                    (root.children[board[i][j]], i, j, 1 << (i * len(board[0]) + j))
                )
    found = []
    while Q:
        node, i, j, visited = Q.pop()
        if node.word:
            found.append(node.word)
            node.word = ""
        if not node.children:
            continue
        lst = np.array([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
        msk = np.array([i > 0, i < len(board) - 1, j > 0, j < len(board[0]) - 1])
        for x, y in lst[msk]:
            if (
                not visited & (1 << (x * len(board[0]) + y))
                and board[x][y] in node.children
            ):
                Q.append(
                    (
                        node.children[board[x][y]],
                        x,
                        y,
                        visited | (1 << (x * len(board[0]) + y)),
                    )
                )

    return found


class Node:
    def __init__(self):
        self.children = {}
        self.word = ""


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]

words = ["oath", "pea", "eat", "rain"]

print(findWords(0, board, words))
