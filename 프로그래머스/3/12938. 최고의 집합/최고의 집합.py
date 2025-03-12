def solution(n, s):
    if s < n: 
        return [-1]

    quotient = s // n
    
    answer = [quotient] * n
    
    for i in range(s % n):
        answer[-(i+1)] += 1

    return answer