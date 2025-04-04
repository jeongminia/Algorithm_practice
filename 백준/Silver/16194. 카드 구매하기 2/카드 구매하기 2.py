import sys

# 입력 처리
input = sys.stdin.read
data = input().splitlines()

goal = int(data[0])
money = list(map(int, data[1].split())) 

dp = [float('inf')]*(goal+1)
dp[0] = 0
#dp[1] = money[0]*goal


for i in range(1, goal + 1):  # 목표 카드 수 i
    
    for j in range(i):        # j = 0부터 i-1까지
        #print(j,";", dp[i], "     ", dp[j] ,'+', money[i-j-1],'=', dp[j] + money[i-j-1])
        dp[i] = min(dp[i], dp[j] + money[i-j-1])
  
    #print(i, '----', dp)


print(dp[-1])