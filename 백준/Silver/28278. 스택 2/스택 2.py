import sys
from collections import deque

# 입력 처리
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
command = deque(data[1:])  
lst = []

while command:
    c = command.popleft()  
    if c[0] == '1':  
        lst.append(int(c[2:]))
    elif c[0] == '2':  
        print(lst.pop() if lst else -1)
    elif c[0] == '3':  
        print(len(lst))
    elif c[0] == '4': 
        print(0 if lst else 1)
    elif c[0] == '5':  
        print(lst[-1] if lst else -1)
