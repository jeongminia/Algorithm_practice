import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()
special = deque(data[0])
bomb = data[1]

word = []

while special:
    k = special.popleft()
    word.append(k)
    if "".join(word[-len(bomb):]) == bomb:
        del word[-len(bomb):]

    #print(word)


if len(word) == 0:
    print("FRULA")
else:
    print("".join(word))