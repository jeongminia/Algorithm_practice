from itertools import permutations

def solution(spell, dic):
    spell_lst = ["".join(i) for i in permutations(spell)]
    
    answer = 0
    for i in spell_lst:
       # print(i)
        if i in dic:
            answer += 1
        else:
            answer += 0
    
    if answer > 0:
        return 1
    else:
        return 2