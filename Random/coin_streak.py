import random
import time

# Code to estimate the expected number of flips to find n heads in a row
# n = 3 E(n) = 14

# HHH  1/8
# HHT  1/8
# HT  1/4
# T 1/2
# E(S) = 3 * 1/ 8 + 1/8 * (E(S) + 3) + 1/4 * (E(S) + 2) + 1/2 * (E(S) + 1)
# E = 3/8 + 3/8 + E/8 + E/4 + 2/4 + E/2 + 1/2
# E(1 - 1/8 - 1/4 - 1/2) = 3/8 + 3/8 + 2/4 + 1/2
# E = 3 + 3 + 4 + 4 = 14


def e_n(n=3, N=1000000):
    # expected number of flips to find 3 heads in a row
    # N simulations
    # average returned
    sum_streaks = 0
    for _ in range(N):
        n_heads = 0
        n_streak = 0
        while n_heads < n:
            if random.random() > 0.5:
                n_heads += 1
            else:
                n_heads = 0
            n_streak += 1
        sum_streaks += n_streak

    return sum_streaks / N


def e_n_v2(n=3, N=10000):
    # rather than restarting each time
    # uses every single flip as a new trial
    # when we reach 3 heads in a row and this current streak is length s
    # add 3 + 4 + ... + s to the sum
    # before resetting n_heads and n_streaks to 2
    # slight problem is that the trials are not independent
    # however with large N, this should not be a problem
    # there will be more variance in the start
    # however we can do a factor of E more trials with the same number of flips so it should be more accurate
    n_streak = 0
    n_heads = 0
    sum_streaks = 0
    for i in range(1, N + 1):
        if random.random() < 0.5:
            n_heads += 1
        else:
            n_heads = 0
        n_streak += 1
        if n_heads == n:
            sum_streaks += (n_streak - (n - 1)) * (n + n_streak) / 2
            n_heads = n - 1
            n_streak = n - 1
    return sum_streaks / (N - n_streak)


def e_n_v3(n=3, N=1000):
    # same as v2 but finishes the current trial
    i = 0
    n_streak = 0
    n_heads = 0
    sum_streaks = 0
    while i < N or n_streak > (n - 1):
        if random.random() < 0.5:
            n_heads += 1
        else:
            n_heads = 0
        n_streak += 1
        i += 1
        if n_heads == n:
            sum_streaks += (n_streak - (n - 1)) * (n + n_streak) / 2
            n_heads = n - 1
            n_streak = n - 1
    return sum_streaks / (N - n_streak)


def distribution(N=10000):
    n = 3
    from collections import defaultdict
    import matplotlib.pyplot as plt

    streaks = defaultdict(lambda: 0)
    n_streak = 0
    n_heads = 0
    for _ in range(N):
        n_heads = 0
        n_streak = 0
        while n_heads < n:
            if random.random() > 0.5:
                n_heads += 1
            else:
                n_heads = 0
            n_streak += 1
        streaks[n_streak] += 1

    E = sum(k * v / N for k, v in streaks.items())

    plt.bar(streaks.keys(), streaks.values())
    plt.xlim(0, round(E) * 2)
    plt.hlines(
        [N * 1 / 8, N * 1 / 16, N * 7 / 128, N * 13 / 256, N * 3 / 64], 0, round(E) * 2
    )
    plt.show()
    return streaks


# HHH = 1/8
# THHH = 1/16
# ?THHH =  2/32 = 1 /16
# ??THHH = 4 / 64 = 1/16
# ???THHH = (8-1) / 128 = 7/128
# 8 ways to arrange first 3 flips (HHH ends early)
# ????THHH = (16-3) / 256 = 13/256
# 16 ways to arrange first 4 flips (HHHH THHH HHHT end early)
# ?????THHH = (16-3) / 256 = (32 - 8)/ 512 = 24/512 = 3/64
# 32 ways to arrange first 5 flips
# 2 + 2 + 4 end early


def performance(n, N, f, repeats):
    sum_E = 0
    sum_t = 0
    for _ in range(repeats):
        start = time.time()
        sum_E += f(n, N)
        sum_t += time.time() - start
    return sum_E / repeats, sum_t / repeats


if __name__ == "__main__":
    # n = 3
    # N = 100000
    # repeats = 20
    # E, t = performance(n, N, e_n, repeats)
    # print(f"V1: E({n}) = {E} in {t}s for {N} trials and {repeats} repeats")
    # E, t = performance(n, N, e_n_v2, repeats)
    # print(f"V2: E({n}) = {E} in {t}s for {N} flips and {repeats} repeats")
    # N_E = N * round(E)
    # E, t = performance(n, N_E, e_n_v2, repeats)
    # print(f"V2: E({n}) = {E} in {t}s for {N_E} flips and {repeats} repeats")

    # n = 4
    # N = 100000
    # repeats = 20
    # E, t = performance(n, N, e_n, repeats)
    # print(f"V1: E({n}) = {E} in {t}s for {N} trials and {repeats} repeats")
    # E, t = performance(n, N, e_n_v2, repeats)
    # print(f"V2: E({n}) = {E} in {t}s for {N} flips and {repeats} repeats")
    # N_E = N * round(E)
    # E, t = performance(n, N_E, e_n_v2, repeats)
    # print(f"V2: E({n}) = {E} in {t}s for {N_E} flips and {repeats} repeats")

    distribution(1000000)
