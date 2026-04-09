from collections import deque

def solution(priorities, location):
    q = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0
    
    while q:
        max_p = max(q, key=lambda x: x[0])[0]
        
        current = q.popleft()
        
        # 4. 우선순위 비교
        if current[0] < max_p:
            # 더 높은 게 있다면 다시 뒤로 보내기
            q.append(current)
        else:
            # 실행 확정
            answer += 1
            # 만약 방금 실행한 게 내가 찾던 그 인덱스라면
            if current[1] == location:
                return answer