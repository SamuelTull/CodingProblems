# https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/A1?source=facebook
import sys

file_path = sys.argv[1]
file_out = sys.argv[2]

with open(file_path) as f:
    lines = f.read().strip().split("\n")

N = int(lines[0])
for i in range(1, N + 1):
    S, D, K = lines[i].split()
    S = int(S)
    D = int(D)
    K = int(K)
    buns = 2 * (S + D)
    burgers = S + 2 * D

    result = "YES" if (buns > K) and (burgers >= K) else "NO"
    with open(file_out, "a") as f:
        f.write(f"Case #{i}: {result}\n")
