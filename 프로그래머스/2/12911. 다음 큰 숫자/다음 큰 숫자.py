def solution(n):
  #  answer = 0
    n_bin = bin(n)[2:].count('1')
    
    m = n+1
    while True:
        if bin(m).count('1') == n_bin:
            return m
        else:
            m += 1
    
#    return answer
