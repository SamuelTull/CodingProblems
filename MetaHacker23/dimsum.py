import sys

file_path = sys.argv[1]
file_out = sys.argv[2]

with open(file_path) as f:
    lines = f.read().strip().split("\n")

N = int(lines[0])
for i in range(1, N + 1):
    R, C, A, B = lines[i].split()
    R = int(R)
    C = int(C)
    result = "YES" if R > C else "NO"
    with open(file_out, "a") as f:
        f.write(f"Case #{i}: {result}\n")
