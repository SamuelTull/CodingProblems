import random
def jumble(l,s):
    random.shuffle(l)
    while l:
        for i in range(len(s)):
            if s[i] == "x":
                x = l.pop()
                s[i] = x
    return "".join(s)

def main():              
    letters = "MSIAURNBE"  
    string = "xxxxxxxxx"
    letters = list(letters)
    string = list(string)
    assert sum([x == "x" for x in string]) == len(letters)

    while True:
        print(jumble(letters.copy(),string.copy()))

main()