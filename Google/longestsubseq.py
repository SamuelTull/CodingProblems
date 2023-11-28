def memoise(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return wrapper


@memoise
def LSS(s1, s2):
    if s1 == "" or s2 == "":
        return 0
    if s1[0] == s2[0]:
        return 1 + LSS(s1[1:], s2[1:])
    return max(LSS(s1[1:], s2), LSS(s1, s2[1:]))


@memoise
def LSS_return(s1, s2):
    if s1 == "" or s2 == "":
        return (0, "")
    if s1[0] == s2[0]:
        X = LSS_return(s1[1:], s2[1:])
        return (1 + X[0], s1[0] + X[1])
    X1 = LSS_return(s1[1:], s2)
    X2 = LSS_return(s1, s2[1:])
    return X1 if X1[0] > X2[0] else X2


# print(LSS("ABCDEFG", "ADG"))
# print(LSS("ABCDEFG", "ADGH"))
# print(LSS("ABCDEFG", "ADZG"))
print(LSS_return("ABCDEFGFUIEWBUBFIEUQWBFIUWE", "BIFJEWBUBFIUWBFIEWBFUE"))
