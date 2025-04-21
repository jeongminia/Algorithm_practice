import sys
from collections import deque

n, k, m = map(int, sys.stdin.readline().split())
arr = deque([i for i in range(1, n + 1)])
rev = False
rev_count = 0
count = 0

while arr:
    if len(arr) == 1:
        print(arr.popleft())
    else:
        if rev:
            tmp = arr.pop()
            count += 1
        else:
            tmp = arr.popleft()
            count += 1
        
        if count == k:
            print(tmp)
            rev_count += 1
            count = 0
        else:
            if rev:
                arr.appendleft(tmp)
            else:
                arr.append(tmp)
        
        if rev_count == m:
            rev = not rev
            rev_count = 0