def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
 #   print(score)
    
 #   print(boxes) # 최대 박스 수
    
    for i in range(m - 1, len(score), m):   # m-1부터 m칸씩
     #   print(score[i], i)
        answer += score[i] * m
    
    return answer