from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for item in skill_trees:
        check = deque(skill)
        
        for i in item:
            if i in check:
                k = check.popleft()
                #print(i, k)
                if i != k:
                    break
        else:
            answer += 1

        

    return answer