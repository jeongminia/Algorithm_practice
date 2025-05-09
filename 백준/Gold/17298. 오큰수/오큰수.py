import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
answer = [-1] * n  # 결과 배열 (-1로 초기화)
stack = []

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        idx = stack.pop()
        answer[idx] = A[i]
    stack.append(i)

print(*answer)