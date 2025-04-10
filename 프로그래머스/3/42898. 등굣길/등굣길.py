def solution(m, n, puddles):
    dp = [[0]*(m) for i in range(n)]
    dp[0][0] = 1

    for i in range(m):       
        for j in range(n):   
            if [i+1, j+1] in puddles:
                dp[j][i] = 0

            # 음수 인덱스 해결
            else:
                if j > 0:
                    dp[j][i] += dp[j-1][i]
                if i > 0:
                    dp[j][i] += dp[j][i-1]

    return dp[-1][-1] % 1000000007