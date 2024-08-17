def solution(d, budget):
    d = sorted(d, reverse=True)
    answer = 0
    
    for i in range(len(d)):
        budget -= d.pop()
        if budget >= 0:
            answer += 1
    
    return answer