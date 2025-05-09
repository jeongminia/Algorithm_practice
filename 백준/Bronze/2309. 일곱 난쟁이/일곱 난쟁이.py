from itertools import combinations

heights = [int(input()) for _ in range(9)]
total = sum(heights)

for i in combinations(heights, 2):
    part = sum(i)
    if total - part == 100:
        target = i
        break

for h in target:
    heights.remove(h)

heights.sort()
for h in heights:
    print(h)