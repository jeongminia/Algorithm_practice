from collections import deque

def solution(priorities, location):
    
    # 값 복사 :  인덱스 값 저장해서 위치 도출 [[2, 0], [1, 1], [3, 2], [2, 3]]
    q = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    
    # 값 크기대로 정렬 [3 2 2 1]
    #p = deque(sorted(priorities, reverse = True))
    
    answer = 0 
    
    while q:
        current = q.popleft()
        # 현재 프로세스보다 우선순위가 높은 프로세스가 큐에 남아 있는지 확인
        if any(current[0] < item[0] for item in q):
            q.append(current)  # 현재 프로세스를 다시 큐에 넣음
        else:
            answer += 1  # 프로세스를 실행
            if current[1] == location:  # 몇번째 실행인지 반환
                return answer

    return answer