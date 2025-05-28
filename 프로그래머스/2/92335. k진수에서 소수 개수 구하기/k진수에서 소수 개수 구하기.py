import math
from collections import deque

# 진수 계산기
def convert(n, k):
    if n == 0:
        return '0'
    else:
        result = ''
        while n > 0:
            result = str(n % k) + result
            n //= k
        return result

# 소수 판별기
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
    
def solution(n,k):
    
    base_k = convert(n, k)
    candidates = base_k.split('0') # deep하게 생각할 필요 없이 0이 있다면 모두 제거?
    print(candidates)
    
    count = 0
    for i in candidates:
        if i == '':
            continue
        if is_prime(int(i)):
            count += 1
    return count
