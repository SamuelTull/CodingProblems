def memoise(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        # print(args, cache[key])
        return cache[key]

    return wrapper


# @memoise
def lcm_math(a, b):
    import math

    return abs(a * b) // math.gcd(a, b)


# @memoise
def lcm(x, y):
    lcm = max(x, y)
    while True:
        if (lcm % x == 0) and (lcm % y == 0):
            return lcm
        lcm += max(x, y)


@memoise
def sets(d, n, l):
    # number of lists in l
    # size n
    # common factors d
    # where each element divides next

    # sets(d,n,l) = sets with l[0] in sets without l[0] in
    #            = sets(d*l[0],n-1,l[1:]) + sets(d,n,l[1:])
    if n == 1:
        return len([x for x in l if x % d == 0])
    if len(l) == n:
        if lcm(d, l[0]) != l[0]:
            return 0
        if [i for i in range(len(l) - 1) if lcm(l[i], l[i + 1]) != l[i + 1]]:
            return 0
        return 1
    if len(l) < n:
        return 0
    if l[0] % d != 0:
        s1 = 0
    else:
        s1 = sets(lcm(d, l[0]), n - 1, l[1:])
    s2 = sets(d, n, l[1:])
    """print(
        f"sets({d}, {n}, {l}) = sets({lcm(d, l[0])}, {n-1}, {l[1:]}) + sets({d}, {n}, {l[1:]}) = {s1}+{s2} "
    )"""
    return s1 + s2


def solution(l):
    return sets(1, 3, l)


def test_sol():
    sets(1, 2, [4, 5, 6])


def run_tests():
    tests = [[1, 2, 3, 4, 5, 6]]
    for test in tests:
        print(test, solution(test))


# test_sol()
run_tests()
