def solution(array, commands):
    answer = []
    
    for lst in commands:
        s = lst[0]-1
        e = lst[1]
        i = lst[2]
        
        ary = array[s:e]
        ary.sort()
        answer.append(ary[i-1])
      #  print(ary)
    
    return answer