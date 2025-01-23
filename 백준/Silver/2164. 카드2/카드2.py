import sys
from collections import deque

input = sys.stdin.read
data = input()
card = int(data)

temp = deque([i for i in range(1, card+1)])
while len(temp) != 1:
    temp.popleft()
    back = temp.popleft()
    temp.append(back)

print(temp[0])