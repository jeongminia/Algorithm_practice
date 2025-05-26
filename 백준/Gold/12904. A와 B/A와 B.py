from collections import deque

S = input().strip()
T = input().strip()

def solution(S, T):
    q = deque([T])
    #print(q)

    while q :
        x = q.pop()
       # print(x)
        
        if x == S :
            return 1
            exit()
            
        if len(x) == len(S) :
            continue
        
        if x[-1] == 'A' :
            q.append(x[:-1])
            
        if x[-1] == 'B' :
            q.append(x[:-1][::-1])
    return 0

print(solution(S, T))