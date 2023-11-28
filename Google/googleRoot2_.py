root2 = 2**0.5

# Sn = /sum_i=1^n (root2 i)
# r = root(2)
# s = 2 + root(2)

# f(x) = x * root(2)


def complementary(n):
    s = 0
    for i in range(n + 1):
        s += 2 + root2
    return s


def exact(n):
    # arithmetic sum formula
    # root2 + 2*root2 + 3*root2 +...+ n*root2
    return n * (1 + n) * root2 / 2


def perfect_solution(n):
    # loops and added
    # cant use for large n
    s = 0
    for i in range(n + 1):
        s += int(i * root2)
    return s


def approx(n):
    # noticed that calculating exact - perfect was ~ n/2
    return int(exact(n) - n / 2 + 0.5)


def solution(n):
    n = int(n)
    if n < -1:
        return str(perfect_solution(1, n))
    sols = []
    for repeat in range(100):
        appr = approx(n - repeat)
        extra = sum(int(i * root2) for i in range(n - repeat + 1, n + 1))
        sols.append(appr - extra)
    return str(max(sols, key=sols.count))


for i in range(1000):
    print(
        i,
        perfect_solution(i),
        exact(i),
        int(exact(i)) - perfect_solution(i),
        complementary(i),
    )
