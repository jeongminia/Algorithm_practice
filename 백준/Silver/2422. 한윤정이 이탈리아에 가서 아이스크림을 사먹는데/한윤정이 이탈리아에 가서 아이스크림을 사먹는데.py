import sys
from itertools import combinations

input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split()) 
icecreams = list(range(1, N + 1))  
ingredients = set(tuple(map(int, line.split())) for line in data[1:M+1])  

cnt = 0

for a, b, c in combinations(icecreams, 3):
    if (a, b) in ingredients or (b, a) in ingredients:
        continue
    if (a, c) in ingredients or (c, a) in ingredients:
        continue
    if (b, c) in ingredients or (c, b) in ingredients:
        continue
    cnt += 1

print(cnt)
