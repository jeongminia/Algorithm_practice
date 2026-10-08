from collections import Counter

def solution(participant, completion):
    answer = ''
    
    part = Counter(participant)
    for person in completion:
        part[person] -= 1
    
    for name, cnt in part.items():
        if cnt > 0:
            return name