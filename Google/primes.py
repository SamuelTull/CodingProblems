import time


def primes_method5(n):
    out = list()
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p] and sieve[p] % 2 == 1:
            out.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return out


def primes(n):
    out = [2]
    sieve = [True] * (n + 1)
    for p in range(3, n + 1, 2):
        if sieve[p]:
            out.append(p)
            for i in range(p, n + 1, 2 * p):
                sieve[i] = False
    return out


def primes_method4(n):
    out = list()
    out.append(2)
    for num in range(3, n + 1, 2):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            out.append(num)
    return out


def timeFN(test, f, n):
    st = time.time()
    primes = f(n)
    et = time.time()
    correct = primes == primes_method5(n)
    elapsed_time = et - st
    print(f"{test}: Found {n} primes in {elapsed_time}, Solution correct: {correct}")


tests = {"Method5": primes_method5, "Optimal": primes}
for n in [100000, 1000000, 10000000]:
    for test, f in tests.items():
        timeFN(test, f, n)
    print()
