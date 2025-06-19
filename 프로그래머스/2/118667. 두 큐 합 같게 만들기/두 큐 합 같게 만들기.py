from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2) # 각 큐의 합
    count = len(queue1) + len(queue2) + 2 # 최대 이동 횟수
    answer = 0
    
    if (sum1 + sum2) % 2 == 1:
        return -1
    
    # 두 큐의 합이 같아질 때까지 반복
    while sum1 != sum2:        
        if count > 0:
            # 합이 큰 쪽에서 원소를 추출하여 다른 쪽에 추출한 원소 추가
            if sum1 < sum2:
                i = queue2.popleft()
                queue1.append(i)
                sum2 -= i
                sum1 += i
                count -= 1
                answer += 1

            elif sum1 > sum2:
                i = queue1.popleft()
                queue2.append(i)
                sum1 -= i
                sum2 += i
                count -= 1
                answer += 1
        
        # 최대 이동 횟수 초과시 -1 리턴
        else:
            return -1
            
    return answer