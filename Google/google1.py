import time


def solution(n):

    primes = [2]
    sieve = [True] * (25000 + 1)
    for p in range(3, 25000 + 1, 2):
        if sieve[p]:
            primes.append(p)
            for i in range(p, 25000 + 1, 2 * p):
                sieve[i] = False

    s = "".join(str(p) for p in primes)
    return s[n : n + 5]


print(solution(3))
print(solution(0))
