def solution(a, b):
    lst = sorted([a, b])
    answer = 0
    
    for i in range(lst[0], lst[1]+1):
        answer += i

    return answer