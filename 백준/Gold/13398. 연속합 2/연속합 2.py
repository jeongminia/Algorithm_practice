N = int(input())
num = list(map(int, input().split()))

dp = [[0]*2 for _ in range(N)]

dp[0][0] = num[0]   
dp[0][1] = float('-inf') 

# DP 채우기
for i in range(1, N):
    # 제거 X
    dp[i][0] = max(dp[i-1][0] + num[i], num[i])

    # 제거 O
    dp[i][1] = max(dp[i-1][1] + num[i], dp[i-1][0])

answer = max(max(x) for x in dp)
print(answer)
