from utils import *
import sys

num_sets = len(set(sets.values()))
max_n = max(placed_original.keys())
N = 10


def solve(n, pos):
    if set_sums[sets[pos]] > set_sum:
        return False
    if set_sum > set_sums[sets[pos]] > set_sum - (n + 1):
        return False

    nums_to_place = max_n - (n + 1)
    if nums_to_place < num_sets:
        spaces = 0
        for i in range(num_sets):
            spaces += (set_sum - set_sums[i]) // (n + 1)
        if spaces < nums_to_place:
            return False

    if n == max_n:
        return all(set_sums[i] == set_sum for i in range(num_sets))

    moves = get_moves(pos, N)
    if n + 1 in placed:
        if placed[n + 1] in moves:
            return solve(n + 1, placed[n + 1])
        else:
            return False
    for move in moves:
        if move in placed.values():
            continue
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
    set_sum = sum_max_n / num_sets
    print("Trying max_n = ", max_n, " and set_sum = ", set_sum)

    for x, y in sorted(get_moves(placed_original[2], N), reverse=True):
        placed = {k: v for k, v in placed_original.items()}
        set_sums = [0 for _ in range(num_sets)]
        placed[1] = (x, y)
        for n, (x, y) in placed.items():
            set_sums[sets[(x, y)]] += n

        if solve(1, (x, y)):
            print("Solved!", max_n, x, y)
            draw_grid(N, placed)
            largest = [0 for _ in range(N)]
            for n, (x, y) in placed.items():
                largest[y] = max(largest[y], n)
            print(sum(x**2 for x in largest))
            sys.exit()

        else:
            print("Not solved! for max_n = ", max_n, " and 1 = ", x, y)
