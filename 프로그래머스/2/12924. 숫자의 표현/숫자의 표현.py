def solution(n):
    answer = []
    k = 0
    
    while True:
        k += 1
        if int((2*n/k + 1 -k)/2) < 0:
            break
            
        if (int((2*n/k + 1 -k)/2) == (2*n/k + 1 -k)/2) and int((2*n/k + 1 -k)/2) > 0:
            answer.append(k)
            
    return len(answer)

# k(2x+k−1) /2 = 15
# k(2x+k−1) = 30

 
