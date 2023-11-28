def solve(A, B, C):
    # A = price of S bBb
    # B = price of D bBBb
    # C = total money
    K = 0
    # S = 0 (A >> B/2)
    D = C // B
    k1 = 2 * D - 1
    K = max(K, 2 * D - 1)

    # S = 1 (A > B/2)
    D = (C - A) // B
    k2 = 2 * D + 1
    K = max(K, 2 * D + 1)

    # S = 2
    D = (C - 2 * A) // B
    k3 = 2 * D + 2
    K = max(K, 2 * D + 2)

    # no need to check S>=3
    # if 3S and ND better than 1S and (N+1)D
    # then 2S better than 1D
    # so just replace all D with 2S

    # D = 0
    S = C // A
    k4 = S
    K = max(K, S)

    # k3 > rest
    # 2 * [ (C - 2 * A) // B ] + 2
    # > 2 * [ (C - A) // B ] + 1
    # > 2 * [ C // B ] - 1
    # > C//A

    return K, [k1, k2, k3, k4]


print(solve(2, 3, 5))
print(solve(2, 3, 2))
print(solve(2, 3, 1))
print(solve(5, 1, 100))
print(solve(1, 3, 100))
print(solve(1, 1, 1000000000000))

print(solve(100, 2, 100))  # case 1
print(solve(11, 20, 1011))  # case 2 B/2 < A but can can afford one more S
print(solve(3, 4, 10))  # case 3 B/2 < A but can can afford 2 more S
print(solve(0.9, 2, 100))  # case 4 B/2 > A
# A < B/2 -> K4
