def solution(cap, n, deliveries, pickups):
    # 먼 거리부터 탐색
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    answer = 0
    
    d, p = 0, 0     
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        
        # 음수가 될 때까지 배달 및 수거 작업
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2
    return answer