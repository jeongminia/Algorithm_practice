from collections import deque
import sys

data = sys.stdin.read().splitlines()
times = list(map(int, data[1].split()))
times.sort()
waitings = deque(times)

total = 0 
answer = 0

while waitings:
    t = waitings.popleft()
    total += t
    answer += total

print(answer)