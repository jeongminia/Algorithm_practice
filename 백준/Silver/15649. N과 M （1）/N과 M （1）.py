from itertools import permutations
import sys

N, M = map(int, sys.stdin.read().split())
num = [str(j+1) for j in range(N)]

for i in permutations(num, M):
    print(" ".join(i))