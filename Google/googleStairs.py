"""
stairs(H,L) = number of ways to partition L bricks into distinct parts >= H
stairs(H,L) 
        = # partitions with H + # partitions without H
        = stairs(H+1,L-H)     + stairs(H+1,L)
stairs(L,L) = 1
stairs(H,<H) = 0

# still have # ## ### #### to remove
# take away L ? 

stairs(H+1,)
"""
from time import perf_counter


def get_time(f):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        ret = f(*args, **kwargs)
        end_time = perf_counter()
        total_time = round(end_time - start_time, 5)
        print("Time", total_time, "seconds")
        return ret

    return wrapper


def stairs(H, L, memo):
    if (H, L) not in memo:
        if H == L:
            s = 1
        elif L < H:
            s = 0
        else:
            s = stairs(H + 1, L - H, memo) + stairs(H + 1, L, memo)
        memo[(H, L)] = s
    return memo[(H, L)]


@get_time
def solution(f, L):
    memo = {}
    return stairs(1, L, memo) - 1


for test in [200]:
    print(test, solution(stairs, test))
