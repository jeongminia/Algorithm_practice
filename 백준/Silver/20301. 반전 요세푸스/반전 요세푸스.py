from collections import deque

n, k, m = map(int, input().split())

cnt = 0
direction = 1 
lst = deque(range(1, n+1)) 

while lst:
    if direction == 1:
        for i in range(k-1):
            lst.append(lst.popleft())
        print(lst.popleft())

    else:
        for i in range(k-1):
            lst.appendleft(lst.pop())
        print(lst.pop())
    
    cnt += 1

    if cnt == m: 
        direction *= -1
        cnt = 0 