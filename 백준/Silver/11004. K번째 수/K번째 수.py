import sys

# 첫 번째 줄 입력: N과 K를 받음
N, K = map(int,  sys.stdin.readline().split())

# 두 번째 줄 입력: A 배열을 받음
A = list(map(int, sys.stdin.readline().split()))

A.sort()
print(A[K-1])