def solution(prices):
    n = len(prices)
    answer = [0] * n 

    for i in range(n):
        time = 0  
        for j in range(i + 1, n):  
            time += 1
            if prices[i] > prices[j]: 
            #    print(prices[i], prices[j])
                break
        answer[i] = time  

    return answer
