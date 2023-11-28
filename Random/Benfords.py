count = {str(i): 0 for i in range(1, 10)}

for j in range(1, 11):
    N = 100_000 * j

    for i in range(1, N):
        count[str(i)[0]] += 1

for i, v in count.items():
    print(i, v, f"{v / sum(count.values()):.2f}%")


count = {str(i): 0 for i in range(1, 10)}
N = 100_000_000_000
for i in range(1, N):
    count[str(i)[0]] += 1

for i, v in count.items():
    print(i, v, f"{v / sum(count.values()):.2f}%")
