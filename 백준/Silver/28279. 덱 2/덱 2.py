import sys
from collections import deque

# 입력 처리
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
command = deque(data[1:])

q = deque() 

while command:
    c = command.popleft()
    #print(q)
    if c[0] == '1':
        q.appendleft(int(c[2:]))
    elif c[0] == '2':
        q.append(int(c[2:]))

    elif c == '3':
        print(q.popleft() if q else -1)
    elif c == '4':
        print(q.pop() if q else -1)

    elif c == '5':
        print(len(q))

    elif c == '6':
        print(0 if q else 1)
    elif c == '7':
        print(q[0] if q else -1)
    elif c == '8':
        print(q[-1] if q else -1)
