def solution(k, m, score):
    score = sorted(score, reverse=True)
    answer = [min(score[i:i+m])*m for i in range(0, m*(len(score)//m), m)]
    
    return sum(answer)