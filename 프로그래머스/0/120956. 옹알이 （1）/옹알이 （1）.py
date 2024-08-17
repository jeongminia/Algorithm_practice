from itertools import permutations

def solution(babbling):
    answer = 0
    say_lst = []
    for j in range(5):
        for i in permutations(["aya", "ye", "woo", "ma"], j):
            say_lst.append("".join(i))
    
    while babbling:
        if babbling.pop() in say_lst:
            answer += 1
            
    return answer