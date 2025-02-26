import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])  # 사람 수
L = list(map(int, data[1].split()))  
J = list(map(int, data[2].split())) 

dp = [0] * 101  

if n == 1:
    if L[0] < 100: 
        print(J[0])
    else:
        print(0)
    exit()

# DP 점화식 적용
for i in range(n):  
    for j in range(99, L[i] - 1, -1):  # 체력 100 초과 X
        dp[j] = max(dp[j], dp[j - L[i]] + J[i])

print(max(dp))  # 최대 기쁨 출력