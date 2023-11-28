# https://en.wikipedia.org/wiki/Beatty_sequence

root2 = 14142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
root2_plus2 = 34142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
# 100 digits


def S(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    N = n * root2 // (10**100)
    m = N * (10**100) // root2_plus2
    return int((N * (1 + N) / 2) - S(m) - m * (m + 1))


def solution(n):
    n = int(n)
    return str(S(n))
