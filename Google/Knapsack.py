def memoise(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return wrapper


@memoise
def KS0_1(N, l):
    if N == 0:
        return 1
    if N < 0 or not l:
        return 0
    return KS0_1(N - l[0], l[1:]) + KS0_1(N, l[1:])


@memoise
def KS_unbound(N, l):
    if N == 0:
        return 1
    if N < 0 or not l:
        return 0
    return KS_unbound(N - l[0], l) + KS_unbound(N, l[1:])


def solution(N, l, unbound):
    if unbound:
        l = list(set(l))
        l.sort(reverse=True)
        return KS_unbound(N, l)
    else:
        l.sort(reverse=True)
        return KS0_1(N, l)
    # return KS(N, l)


test = [5, [1, 2, 3], True]
print(solution(*test))
from numpy.random import randint

test = [1000, randint(0, 100, 50).tolist(), True]
print(solution(*test))
