def solution(storey):
    answer = 0

    while storey > 0:
        k = storey % 10 
     #   print(k)
        storey //= 10  # 몫만 가져가서 저장
        
        if k > 5:  
            answer += (10 - k)
            storey += 1 
        elif k < 5:  
            answer += k
        else:  
            if storey % 10 >= 5: 
                answer += (10 - k)
                storey += 1
            else:
                answer += k 

      #  print(answer, storey, '----')

    return answer
