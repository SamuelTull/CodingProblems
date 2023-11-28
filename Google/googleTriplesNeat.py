def memoise(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)

        return cache[key]

    return wrapper


def lcm(x, y):
    lcm = max(x, y)
    while True:
        if (lcm % x == 0) and (lcm % y == 0):
            return lcm
        lcm += max(x, y)


def sets(d, n, l):
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
    return s1 + s2


def solution(l):
    return sets(1, 3, l)


import numpy as np


def run_tests():
    tests = [[], [1999, 132]]
    tests += [list(np.random.randint(1, 999999, 2000))]
    for test in tests:
        print(test, solution(test))


run_tests()


# test_sol()
run_tests()
