import sys
from collections import deque

# 입력 처리
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
command = data[1:]

q = deque()  

for c in command:
    if c[:4] == 'push':  
        q.append(int(c[5:]))
    elif c == 'front':  
        print(q[0] if q else -1)
    elif c == 'back':  
        print(q[-1] if q else -1)
    elif c == 'size': 
        print(len(q))
    elif c == 'pop': 
        print(q.popleft() if q else -1)
    elif c == 'empty':  
        print(0 if q else 1)
