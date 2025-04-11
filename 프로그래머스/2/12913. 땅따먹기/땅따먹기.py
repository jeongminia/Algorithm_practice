def solution(land):
    answer = 0

    # 매 줄마다 누적해서 최대의 점수 이어가기
    dp = [[-1]*4 for i in range(len(land)) ]
   
    
    dp[0] = land[0]

    

    for i in range(1, len(land)):
        for j in range(4):
            max_value = 0
            for k in range(4):         # 이전 줄의 모든 열을 순회
                if k != j:             # 지금 열(j)과 같은 열은 건너뛰고
                    max_value = max(max_value, dp[i-1][k])  

            dp[i][j] = max_value + land[i][j]


    return max(dp[-1])