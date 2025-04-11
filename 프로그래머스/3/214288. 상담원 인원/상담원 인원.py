import heapq
from itertools import product

def calc_wait_time(requests, num_mentors):
    requests.sort()
    heap = []
    total_wait = 0

    for start, duration in requests:
        if len(heap) < num_mentors:
            heapq.heappush(heap, start + duration)
        else:
            available = heapq.heappop(heap)
            wait = max(0, available - start)
            total_wait += wait
            heapq.heappush(heap, start + duration + wait)

    return total_wait

def solution(k, n, reqs):
    base = [1] * k  # 최소 1명씩 배치
    n = n-k

    con_lst = [[] for _ in range(k)] # 상담 유형에 따라 사람 저장
    
    for s, e, t in reqs:
        con_lst[t-1].append([s, e])

    print(con_lst)
    
    # 참가자가 상담을 요청했을 때부터 상담을 시작하기까지 기다린 시간의 합이 최소가 되도록 멘토인원 정하기
    answer = float('inf')
    
    # 모든 상담 유형에 남은 인원 분배 (product는 중복순열)
    for assign in product(range(n + 1), repeat=k):
        if sum(assign) != n:
            continue  # 전체 상담원 수 초과

        # 최종 상담원 배치: 최소 1명 + 추가 인원
        mentor = [b + a for b, a in zip(base, assign)]

        total_wait = sum(
            calc_wait_time(con_lst[i], mentor[i])
            for i in range(k)
        )

        answer = min(answer, total_wait)

    return answer