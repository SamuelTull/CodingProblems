import time


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


"""
321  0 1 2 
312  0 2 1 
231  1 0 2
213  1 2 0
132  2 0 1 
123  2 1 0

x0x1x
x1x0x


"""


def codes_old(b):
    cs = [""]
    for i in range(b):
        n = len(cs)
        l = len(cs[0])
        new_cs = []
        for c in cs:
            for ipos in range(l + 1):
                # inserting i into cs[idx] at position ipos
                new_cs.append("".join((c[:ipos], str(i), c[ipos:])))
        cs = new_cs
    cs.sort()
    return cs


def solution(s):
    cs = [""]
    for i in range(len(s)):
        n = len(cs)
        l = len(cs[0])
        new_cs = []
        for c in cs:
            for ipos in range(l + 1):
                # inserting i into cs[idx] at position ipos
                new_cs.append("".join((c[:ipos], str(s[i]), c[ipos:])))
        cs = new_cs
    cs.sort(reverse=True)

    N = len(cs[0])
    while N > 0:
        for ci in cs:
            if int(ci[:N]) % 3 == 0:
                return int(ci[:N])
        N -= 1
    return 0


tests = [[3, 1, 4, 1], [3, 1, 4, 1, 5, 9]]
for test in tests:
    print(test, solution(test))
