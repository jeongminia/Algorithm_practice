def solution(s, skip, index):
    answer = ''
    alpabet = "abcdefghijklmnopqrstuvwxyz"*10
    
    for i in s:
        start = alpabet.index(i)+1
        
        part = ""
        while len(part) != index:
            if alpabet[start] not in skip:
                part+=alpabet[start]
                
            start+=1
            
        answer += part[-1]
    
    return answer