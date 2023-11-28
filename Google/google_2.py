# "https://foobar.withgoogle.com/?eid=IkpNJ"

"""
12 x1 x2 14 x2 x3 6

x1 = 2* x3 
x1 + x2 

r_0 = 2*r_2
r_1 = d0 - r_0
r_2 = d1 - (d0 - r_0)  = d1 - d0 + r_0

r_0  = d1 - d0 / (-0.5)
r_0  = -d1 + d0 / (0.5)

r_2 = d1 - (d0 - r_0)  = d1 - d0 + 2*r_3
r_3 = d2 - d1 + d0 - r_0 
r0 = d2 - d1 + d0  / (1.5)

n = len(dist)
n odd  -even + odd   /  0.5  (x 2)
n even even - odd +  /  1.5  (x 3/2)

(1 - 2)* r_n

"""


def solution_old(s):
    dist = [s[i] - s[i - 1] for i in range(1, len(s))]
    n = len(dist)
    num = sum((-1) ** (i % 2) * dist[i] for i in range(n))
    if num <= 0:
        return -1, -1
    if n % 2 == 0:
        return int(2 * num), 1
    else:
        if num % 3 == 0:
            return int(num * 2 / 3), 1
        else:
            return int(num * 2), 3


def solution(s):
    def getR(R_0, dist):
        R = [R_0]
        for i in range(len(dist)):
            R.append(dist[i] - R[-1])
        return R

    dist = [s[i] - s[i - 1] for i in range(1, len(s))]
    n = len(dist)
    num = sum((-1) ** (i % 2) * dist[i] for i in range(n))
    # if n odd (even), r0 = num*2/3  (=num*2)
    if n % 2 == 0:
        R = getR(2 * num, dist)
        if [x for x in R if x <= 0]:
            return -1, -1
        return int(2 * num), 1
    else:
        R = getR(2 * num / 3, dist)
        if [x for x in R if x <= 0]:
            return -1, -1
        if num % 3 == 0:
            return int(num * 2 / 3), 1
        else:
            return int(num * 2), 3


tests = [
    [0, 4, 7, 9],
    [-9, -7, -4, 0],
    [-9, -5, -2, 0],
    [4, 17, 50],
    [4, 30, 50],
    [0, 1],
    [0, 3],
    [2, 8, 12, 14, 15],
]
for test in tests:
    print(test, solution(test))
