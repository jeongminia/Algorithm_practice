def solution(numbers):
    answer = []
    before = [numbers.pop()] 

    answer.append(-1) 
    
    while numbers:
        after = numbers.pop() 
       # print(before) 

        # before 스택의 최상단 값이 after보다 크거나 같을 때
        while before and after >= before[-1]:
            before.pop() 
        
       # print(before)
        
        if before:
            answer.append(before[-1])
        else:
            answer.append(-1)
        
        before.append(after)
    
    return answer[::-1] 
