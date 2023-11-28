def reverse(x: int):
    x = str(x)
    x = x[::-1]
    return int(x)


def palindrome(x: int):
    x = str(x)
    return x == x[::-1]


import sys

if len(sys.argv) == 1:
    x = input("Number? ")
else:
    x = sys.argv[1]

x = int(x)
print(x)
seen = set()

while x not in seen and not palindrome(x):
    seen.add(x)
    x += reverse(x)
    print(x)
