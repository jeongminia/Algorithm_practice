# 땅의 높이를 일정하게 변경 
import sys
from collections import Counter

N, M, B = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
flat_ground = dict(Counter([h for row in ground for h in row]))

min_h = min(flat_ground)
max_h = max(flat_ground)

result_time = float('inf')
result_height = 0

for target_h in range(min_h, max_h + 1):
    t = 0
    inventory = B

    for height, cnt in flat_ground.items():
        if height > target_h:
            remove = (height - target_h) * cnt
            t += remove * 2
            inventory += remove
        elif height < target_h:
            add = (target_h - height) * cnt
            t += add * 1
            inventory -= add

    if inventory >= 0:
        if t < result_time or (t == result_time and target_h > result_height):
            result_time = t
            result_height = target_h
    
    # print(target_h, t, inventory)

print(result_time, result_height)