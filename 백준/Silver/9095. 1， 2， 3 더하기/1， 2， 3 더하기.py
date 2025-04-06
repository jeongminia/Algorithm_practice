import sys

input = sys.stdin.read
data = input().splitlines()
test_cases = list(map(int, data[1:]))

special_lst = [1, 2, 3]

dp = [0]*(12) # 경우의 수에서 순서를 고려해서 세고 있음
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    for j in special_lst:
        dp[i] += dp[i-j]

for i in test_cases:
    print(dp[i])