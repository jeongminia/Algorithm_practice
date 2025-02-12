import sys
from itertools import combinations

input = sys.stdin.read
data = input().splitlines()

find_lst = data[0]
target = data[1]

pos = len(target)
cnt = 0

while find_lst:
    # print(find_lst, cnt)
    
    k = find_lst[:pos]
    if k == target:
        find_lst = find_lst[pos:]
        cnt += 1
    else:
        find_lst = find_lst[1:]

print(cnt)