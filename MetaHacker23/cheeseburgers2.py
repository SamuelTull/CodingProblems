# https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/A2
import sys

# A = price of S bBb
# B = price of D bBBb
# C = total money
# no need to check S>=3
# if 3S and ND better than 1S and (N+1)D
# then 2S better than 1D
# so just replace all D with 2S
# Not neccesarly true for S = 2 because of the extra bun
# Only 4 cases so quicker to check all than think when each case occurs s

file_path = sys.argv[1]
file_out = sys.argv[2]

with open(file_path) as f:
    lines = f.read().strip().split("\n")


def solve(A, B, C):
    K = 0
    # S = 0
    D = C // B
    k1 = 2 * D - 1
    K = max(K, 2 * D - 1)

    # S = 1
    D = (C - A) // B
    k2 = 2 * D + 1
    K = max(K, 2 * D + 1)

    # S = 2
    D = (C - 2 * A) // B
    k3 = 2 * D + 2
    K = max(K, 2 * D + 2)

    # D = 0
    S = C // A
    k4 = S
    K = max(K, S)

    return K


N = int(lines[0])
for i in range(1, N + 1):
    A, B, C = lines[i].split()
    A = int(A)
    B = int(B)
    C = int(C)
    K = solve(A, B, C)
    with open(file_out, "a") as f:
        f.write(f"Case #{i}: {K}\n")


# Example that takes each case
# print(solve(100, 2, 100))  # case 1
# print(solve(11, 20, 1011))  # case 2 B/2 < A but can can afford one more S
# print(solve(3, 4, 10))  # case 3 B/2 < A but can can afford 2 more S
# print(solve(0.9, 2, 100))  # case 4 B/2 > A
