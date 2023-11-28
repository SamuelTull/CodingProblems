from time import perf_counter


def get_time(f):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        ret = f(*args, **kwargs)
        end_time = perf_counter()
        total_time = round(end_time - start_time, 2)
        print("Time", total_time, "seconds")
        return ret

    return wrapper


def memoise(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return wrapper


def memoise2(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return wrapper


def memoise3(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return wrapper


@memoise
def lcm_old(x, y):
    lcm = max(x, y)
    while True:
        if (lcm % x == 0) and (lcm % y == 0):
            return lcm
        lcm += max(x, y)


import math


@memoise
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


@memoise
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


@get_time
def solution_1(l):
    return sets(1, 3, l)


@get_time
def solution_2(l):
    @memoise2
    def compare(x, y):
        return l[x] % l[y] == 0

    c = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if compare(j, i) and compare(k, j):
                    c += 1
    return c


@get_time
def solution_copy(l):
    n = len(l)
    arr = [0] * n
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            if l[j] % l[i] == 0:
                arr[i] += 1
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if l[j] % l[i] == 0:
                res += arr[j]
    return res


def solution(l):
    num = [0 for i in range(len(l))]
    for i in range(len(l)):
        for j in range(1 + i, len(l)):
            if l[j] % l[i] == 0:
                num[i] += 1
    total = 0
    for i in range(len(l)):
        for j in range(1 + i, len(l)):
            if l[j] % l[i] == 0:
                total += num[j]
    return total


import numpy as np


def run_big_tests():
    tests = {"sol1": solution_1, "sol2": solution_2, "sol3": solution_copy}
    tests = {"sol3": solution_copy}
    for N in [10, 100, 200, 500, 1000, 1500]:
        l = list(np.random.randint(1, 99999, N))
        for test, f in tests.items():
            print("N", N, test, f(l))
        print()


def run_tests(f):
    tests = [[1, 1, 1, 1], [1, 2, 3, 4, 5, 6]]
    for test in tests:
        print(test, f(test))


run_tests(solution)
