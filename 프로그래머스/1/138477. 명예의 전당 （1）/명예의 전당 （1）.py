from collections import deque

def solution(k, score):
    answer = []
    legend = deque([])
    score = deque(score)
    print(score)
    
    while score:
        a = score.popleft()
        
        if len(legend) < k:
            legend.append(a)
        elif len(legend) == k: 
            if a > min(legend):
                legend.remove(min(legend))  # 최솟값 제거
                legend.append(a)
                
        answer.append(min(legend))
    
    return answer