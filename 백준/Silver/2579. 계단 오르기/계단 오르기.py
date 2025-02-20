import sys
input = sys.stdin.read

data = input().split()
n = int(data[0]) 
stair = list(map(int, data[1:]))  

# DP 배열 초기화
if n == 1:
    print(stair[0])
    exit()

dp = [0] * n
dp[0] = stair[0] 
dp[1] = stair[0] + stair[1]

if n > 2:
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[-1])