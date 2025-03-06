import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
index = 1

test_cases = []

for _ in range(T):
    N, M = map(int, data[index].split())
    priorities = list(map(int, data[index + 1].split()))
    test_cases.append((N, M, priorities))
    index += 2

for test in test_cases:
    N, M, priorities = test  # 문서 개수, 찾고 싶은 문서 위치, 문서 리스트

    queue = deque([(i, p) for i, p in enumerate(priorities)]) 
    sorted_priorities = sorted(priorities, reverse=True) 
    print_order = 0  

    while queue:
        cur = queue.popleft() 

        if cur[1] < sorted_priorities[0]: 
            queue.append(cur) 
        else:
            print_order += 1 
            sorted_priorities.pop(0)  

            if cur[0] == M:  
                print(print_order)
                break