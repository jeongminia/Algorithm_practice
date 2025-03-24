import sys

input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N):
    t, p = schedule[i]
    
    # 이익 유지
    dp[i] = max(dp[i], dp[i-1])
   # print(i,schedules[i],dp)

    # 이익 갱신
    if i + t <= N:
        dp[i + t] = max(dp[i + t], dp[i] + p)

   # print(i,schedules[i],dp)

print(max(dp))