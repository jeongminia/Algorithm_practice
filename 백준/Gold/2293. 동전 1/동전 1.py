import sys
input = sys.stdin.read
data = input().split()

n, k = map(int, data[:2])
coins = list(map(int, data[2:]))

dp = [0] * (k+1)
dp[0] = 1

for i in range(n):  
    for j in range(coins[i], k+1):  
        dp[j] += dp[j-coins[i]]
        #print(dp)

print(dp[k])