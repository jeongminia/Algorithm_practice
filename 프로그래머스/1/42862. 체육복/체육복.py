def solution(n, lost, reserve):
    clothes = [1 + (i + 1 in reserve) - (i + 1 in lost) for i in range(n)]
  #  print(clothes)
    
    for i in range(n):
        if clothes[i] == 0:  
            if i > 0 and clothes[i - 1] == 2: 
                clothes[i - 1] -= 1
                clothes[i] += 1
            elif i < n - 1 and clothes[i + 1] == 2:
                clothes[i + 1] -= 1
                clothes[i] += 1
    
   # print(clothes)
    answer = 0
    for j in clothes:
        if j >= 1:
            answer += 1
            
    return answer