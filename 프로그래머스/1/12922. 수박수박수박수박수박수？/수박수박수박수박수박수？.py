def solution(n):
    
    if n%2 == 1:
        # 홀수이면
        return "수박"*(n//2)+"수"
    else: 
        # 짝수이면
        return "수박"*(n//2)
    
    return answer