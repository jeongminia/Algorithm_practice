import sys

input = sys.stdin.read
data = input().splitlines()
test_cases = list(map(int, data[1:]))

n = max(test_cases)
dp = [0] * (101)  # 최대 100까지 계산

dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

# 출력
for t in test_cases:
    print(dp[t])
