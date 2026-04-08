from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    answer = 0
    while q:
        m = max(q)
        l = q.popleft()
        location -= 1 
        
        if l != m: # 최댓값과 가장 앞에 위치한 프로세스가 일치하지 않는다면
            q.append(l)
            # 내 타겟이 맨 뒤로 이동한다면
            if location < 0:
                location = len(q) -1 
        else: # 최댓값과 가장 앞에 위치한 프로세스가 일치한다면
            answer += 1
            if location < 0:
                break
        
    return answer