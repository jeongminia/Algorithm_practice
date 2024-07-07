def solution(s):
    
    if s[0] == '-':
        answer = 0 - int(s[1:])
    else:
        answer = int(s)
    
    return answer