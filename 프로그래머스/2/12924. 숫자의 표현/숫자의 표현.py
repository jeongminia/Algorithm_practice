def solution(n):
    answer = []
    k = 0
    
    while True:
        k += 1
      #  print((2*n/k + 1 -k)/2)
        
        if (int((2*n/k + 1 -k)/2) == (2*n/k + 1 -k)/2) and int((2*n/k + 1 -k)/2) > 0:
           # answer.append((2*n/k + 1 -k)/2)
            answer.append(k)
        
        if k == n:
            break
    
    return len(answer)

# k(2x+k−1) /2 = 15
# k(2x+k−1) = 30

 
