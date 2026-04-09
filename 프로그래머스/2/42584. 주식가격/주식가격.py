def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        current = prices[i]
        for j in range(i+1,len(prices)):
            if (current > prices[j]):
                m = j-i
                break
            else:
                m = len(prices)-i-1
        
        answer.append(m)
    answer.append(0)
    
    return answer # 가격이 떨어지지 않은 기간은 몇 초인지