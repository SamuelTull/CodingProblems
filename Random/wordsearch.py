from collections import deque


def exist(board, word):
    W = len(board)
    H = len(board[0])
    Q = deque()
    board_set = set(board[r][c] for r in range(W) for c in range(H))
    word_set = set(x for x in word)
    if word_set - board_set:
        return False
    for r in range(W):
        for c in range(H):
            if board[r][c] == word[0]:
                Q.append((r, c, 1, 1 << (H * r + c)))
    while Q:
        r, c, idx, visited = Q.pop()
        if idx == len(word):
            return True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= r + dr < W and 0 <= c + dc < H:
                bw = 1 << (H * (r + dr) + c + dc)
                if not bw & visited:
                    if board[r + dr][c + dc] == word[idx]:
                        Q.append((r + dr, c + dc, idx + 1, visited | bw))
    return False


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
word = "oath"
print(exist(1, board, word))
