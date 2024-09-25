from itertools import permutations

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    n_lst = []
    for j in range(1, len(numbers)+1):
        for i in permutations(numbers, j):
            k = int("".join(i))
            if k not in [0, 1] :
                n_lst.append(k)
    n_lst = list(set(n_lst))
    
    
    answer = 0
    for num in n_lst:
        if is_prime(num):
            answer += 1
    
    return answer