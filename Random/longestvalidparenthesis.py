def memoise(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return wrapper


##################################################
###### thought the substring didnt have to be connected
###### "()(()" is supposed to be 2 not 4
#################################################
def dp_old(s, n):
    # n = #( - #)
    if n < 0:  # if have more ) than ( cannot fix
        return -1e9
    if s == "":
        if n > 0:
            return -1e9
        return 0

    dn = {"(": 1, ")": -1}[s[0]]
    dp1 = dp_old(s[1:], n + dn)  # add s[0]
    dp2 = dp_old(s[1:], n)  # ignore s[0]
    return max(1 + dp1, dp2)


def solution_old(s: str) -> int:
    return dp_old(s, 0)


#####################################################
#######
###################################################


def dp(s, n, N):
    if s == "":
        if n == 0:
            return N
        return -1e9

    if n == 0:
        if s[0] == "(":
            return max(N, dp(s[1:], n + 1, N + 1))
        return N
    dn = {"(": 1, ")": -1}[s[0]]
    return dp(s[1:], n + dn, N + 1)


def solution(s: str) -> int:
    if s == "":
        return 0
    return max(dp(s[i:], 0, 0) for i in range(len(s)))


#####################################################
#######
###################################################
def dp_found(s):
    if s == "":
        return 0
    dp = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == "(":
            continue

        if s[i - 1] == "(":
            if i - 2 < 0:
                dp[i] = 2
            else:
                dp[i] = 2 + dp[i - 2]

        else:
            j = i - 1 - dp[i - 1]
            if j < 0:
                continue
            else:
                if s[j] == "(":
                    if j - 1 >= 0:
                        dp[i] = 2 + dp[i - 1] + dp[j - 1]
                    else:
                        dp[i] = 2 + dp[i - 1]

    return max(dp)


test_print = False
tests = []
validate = [["(()", 2], [")()())", 4], ["()())", 4], ["", 0], ["()(()", 2]]

print("TEST CASES")
for i in range(len(tests)):
    test = tests[i]
    s = solution(test)
    print(f"Test{i}: Answer: {s}")
    if test_print:
        print(test, end="\n\n")

for i in range(len(validate)):
    test, soln = validate[i]
    s = dp_found(test)
    print(
        f"Test{i}: {'PASSED' if soln == s else 'FAILED' }, Answer: {s}, Expected: {soln}"
    )
    if test_print:
        print(test, end="\n\n")
