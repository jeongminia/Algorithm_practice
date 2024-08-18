from collections import deque

def solution(s):
    answer_str = []
    answer = []
    
    q = deque([(priority, idx) for idx, priority in enumerate([s[i] for i in range(len(s))])])
    
    while q:
        k = q.popleft()
        
        if k[0] not in set(answer_str):
            answer.append(-1)
        else:
            answer.append(k[1] - max(list(filter(lambda x: answer_str[x] == k[0], range(len(answer_str))))))
        
        answer_str.append(k[0])


    return answer
