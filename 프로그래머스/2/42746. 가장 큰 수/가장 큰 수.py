from itertools import permutations

def solution(numbers):
    
    num_str = list(map(str, numbers))
    num_str.sort(key = lambda x : x*3,reverse=True)
    
    answer = "" 
    for k in num_str:
        answer += k
    
    return str(int(answer))