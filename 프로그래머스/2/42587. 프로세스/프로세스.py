from collections import deque

   # 1. 맨 앞 꺼내기
   # 2. 더 높은 게 있으면 뒤로
   # 3. 없으면 실행, location이면 반환

def solution(priorities, location):
    dq = deque((p, i) for i, p in enumerate(priorities))  # (우선순위, 원래 위치)
    answer = 0

    while dq:
        cur = dq.popleft()
        print(cur)

        has_higher = False              # 더 높은 게 있나? 일단 없다고 가정
        for other in dq:                # 남은 것들을 하나씩 확인
            if other[0] > cur[0]:       # 나보다 높은 우선순위 발견
                has_higher = True
                break                   # 하나만 찾으면 더 볼 필요 없음
        
      #  print(cur, dq)
        
        if has_higher: # 나보다 높음
            dq.append(cur)
        else: # 나보다 높은게 없음
            answer += 1
            if cur[1] == location:
                return answer