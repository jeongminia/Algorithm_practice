import heapq

def solution(jobs):
    # 작업을 요청 시간이 빠른 순으로 정렬
    jobs.sort()
    time, current_time, n = 0, 0, len(jobs)
    i = 0
    heap = []

    while i < n or heap:
        while i < n and jobs[i][0] <= current_time:
            # 작업의 소요 시간을 기준으로 힙에 추가
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1

        # 힙이 비어있지 않다면 작업을 처리
        if heap:
            job_duration, job_start = heapq.heappop(heap)
            # 현재 시각 갱신
            current_time += job_duration
            # 요청부터 종료까지의 시간을 누적
            time += current_time - job_start
        else:
            current_time = jobs[i][0]

    return time // n