import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # (시간, 음식 번호)

    total = 0
    previous = 0
    length = len(food_times)

    # 가장 시간이 적은 음식부터 round 단위로 제거
    while total + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        total += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - total) % length][1]
