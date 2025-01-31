import math
import sys

# 입력 받기
n, r = map(int, sys.stdin.read().split())

print(math.comb(n-1, r-1))