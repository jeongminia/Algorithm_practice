import sys

n = int(sys.stdin.readline())
road = list(input())
count = 0

for i in range(n-1):
    if road[i] == road[i+1]:
        continue
    else:
        if road[i] == 'W':
            continue
        else:
            count += 1

print(count)