def solution(n):
    lst = [0, 1]
    
    for i in range(2, n+1):
        if i == 2 : 
            answer = sum(lst)
            lst.append(answer)
            
        elif n > i > 2 :
            new_anwser = lst[i-1] + lst[i-2]
            lst.append(new_anwser)
            
        elif i == n :
            anw = lst[i-1] + lst[i-2]
    
    anw = anw % 1234567
     
    return anw