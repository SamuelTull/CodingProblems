from utils import *

placed_original = placed_original_1
sets = sets_1
num_sets = len(set(sets.values()))
max_n = max(placed_original.keys())
N = 5


def solve(n, pos):
    if any(set_sums[i] > set_sum for i in range(len(set_sums))):
        return False
    if n == max_n:
        return all(set_sums[i] == set_sum for i in range(len(set_sums)))

    moves = get_moves(pos, N)
    if n + 1 in placed:
        if placed[n + 1] in moves:
            return solve(n + 1, placed[n + 1])
        else:
            return False
    for move in moves:
        placed[n + 1] = move
        set_sums[sets[move]] += n + 1
        if solve(n + 1, move):
            return True
        del placed[n + 1]
        set_sums[sets[move]] -= n + 1
    return False


for max_n in range(max_n, N * N + 1):
    sum_max_n = sum(range(max_n + 1))
    if sum_max_n % num_sets != 0:
        continue
    else:
        set_sum = sum_max_n / num_sets
        print("Trying max_n = ", max_n, " and set_sum = ", set_sum)

    placed = {k: v for k, v in placed_original.items()}
    set_sums = [0 for _ in range(num_sets)]
    for n, (x, y) in placed.items():
        set_sums[sets[(x, y)]] += n

    if solve(1, (0, 4)):
        print("Solved!")
        draw_grid(N, placed)
        largest = [0 for _ in range(N)]
        for n, (x, y) in placed.items():
            largest[y] = max(largest[y], n)
        print(sum(x**2 for x in largest))
        assert False
    else:
        print("Not solved! for max_n = ", max_n, " and 1 = ", x, y)
