import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(n)]

dp = [float('inf')] * (k+1)
dp[0] = 0 

for i in range(n):  
    for j in range(coins[i], k+1):  
        dp[j] = min(dp[j], dp[j-coins[i]] + 1)
        #print(dp)

print(dp[k] if dp[k] != float('inf') else -1)