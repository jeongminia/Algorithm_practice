from itertools import combinations

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    cnt =0
    answer = [sum(j) for j in combinations(nums, 3)]
    
    for num in answer:
        if is_prime(num):
            cnt += 1
    
    return cnt