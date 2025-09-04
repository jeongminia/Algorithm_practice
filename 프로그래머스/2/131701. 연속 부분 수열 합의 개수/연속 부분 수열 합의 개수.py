from collections import deque
def solution(elements):
    answer=set()
    
    deq=deque(elements)
    
    for i in range(len(deq)):    # i = 0 ~ N-1
        total = 0
        for e in deq:            # e는 현재 deque의 순서대로
            total += e
            answer.add(total)    # 현재 위치에서 누적합 추가
        deq.append(deq.popleft())  # 맨 앞을 뒤로 보내면서 "시작 위치"를 한 칸 회전


    return len(answer)