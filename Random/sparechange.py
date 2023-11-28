for _ in range(int(input())):
    n = int(input())
    if n == 1:
        a = int(input())
        print(a // 3 + (a % 3 != 0))
        continue
    A = list(map(int, input().split()))
    n3 = max(A) // 3
    need = [False, False, False]
    for a in A:
        need[a % 3] = True
    if need[0] and need[1]:
        print(n3 + 1)
        continue
    print(n3 + need[0] + need[2])
