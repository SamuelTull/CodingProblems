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


@memoise
def stairs(H, L):
    if H == L:
        return 1
    if L < H:
        return 0
    return stairs(H + 1, L - H) + stairs(H + 1, L)


@get_time
def solution(L):
    memo = {}
    return stairs(1, L) - 1


test = 200
print(test, solution(test))
