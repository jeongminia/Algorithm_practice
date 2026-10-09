def solution(prices):
    answer = []
    
    for i, a in enumerate(prices):
        
        visited = False
        for j in range(i + 1, len(prices)):
            b = prices[j]
            if a > b: # 가격이 떨어집니다
                answer.append(j-i)
                visited = True
              #  print("가격떨어진대", j-i)
                break
                
        if visited==False:
            # 가격이 떨어지지 않았습니다
            answer.append(len(prices)-i-1)
    

    return answer