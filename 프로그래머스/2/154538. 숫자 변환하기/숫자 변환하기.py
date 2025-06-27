def solution(x, y, n):
    dp = [ -1 for i in range(y*3+1)]
    dp[x] = 0
    
    for i in range(x,y):
        if dp[i] == -1:
            pass
        else:
            # x에 n을 더합니다
            if dp[i+n] != -1:
                dp[i + n] = min(dp[i]+1,dp[i+n]) # 이미 이전에 도달한 적 있는 값이면 더 적은 연산 횟수로 갱신
            else: 
                dp[i+n] = dp[i]+1 # 처음 도달한 경우면 현재 연산 횟수 + 1로 등록
            
            # x에 2를 곱합니다
            if dp[i*2] != -1:
                dp[i*2] = min(dp[i*2], dp[i]+1)
            else: 
                dp[i*2] = dp[i]+1

            # x에 3을 곱합니다
            if dp[i*3] != -1:
                dp[i*3] = min(dp[i*3] , dp[i]+1)
            else: 
                dp[i*3] = dp[i]+1

    return dp[y]