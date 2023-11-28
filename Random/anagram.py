import random
import sys

if len(sys.argv) == 1:
    word = input("Word? ")
else:
    word = sys.argv[1]


chars = [x for x in word]
while True:
    random.shuffle(chars)
    print("".join([x for x in chars]))
