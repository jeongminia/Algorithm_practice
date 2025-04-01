N = int(input())

dp = [-1]*(max(N+1, 4))  # 최소 길이 4 확보
dp[1] = True
dp[2] = False
dp[3] = True

for i in range(4, N+1):
    if not dp[i-1] or not dp[i-3]:  # 상대가 지면 내가 이김
        dp[i] = True
    else:
        dp[i] = False

print("SK" if dp[N] else "CY")
