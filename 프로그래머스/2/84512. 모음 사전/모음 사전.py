from itertools import permutations

def solution(word):
    answer = []   

    for i in range(1, 6):
        for j in permutations(['A', 'E', 'I', 'O', 'U']*5, i):
            answer.append("".join(j))
    answer = sorted(list(set(answer)))
   # print(answer)
    return answer.index(word) + 1