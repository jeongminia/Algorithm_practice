from itertools import permutations

def solution(babbling):
    answer = 0
    say_lst = []
    for j in range(len(babbling)):
        for i in permutations(["aya", "ye", "woo", "ma"], j):
            say_lst.append("".join(i))

 #   print(say_lst)
    
    while babbling:
        a = babbling.pop()
  #      print(a)
        if a in say_lst:
            answer += 1
            
    
    
    return answer