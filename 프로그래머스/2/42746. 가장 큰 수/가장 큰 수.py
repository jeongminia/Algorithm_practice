from itertools import permutations

def solution(numbers):
    
    num_str = list(map(str, numbers))
  #  print(num_str)
    num_str.sort(key = lambda x : x*4,reverse=True)
  #  print(num_str)
    
    answer = "" 
    for k in num_str:
        answer += k
    
    return str(int(answer))