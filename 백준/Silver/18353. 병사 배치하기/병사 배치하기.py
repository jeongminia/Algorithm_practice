from collections import deque

N = int(input())
soldier = list(map(int, input().split()))

soldier.reverse()

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if soldier[j] < soldier[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))