def solution(my_string):
    answer = ''
    
    for j in my_string:
        if j not in answer:
            answer += j
    
    return answer