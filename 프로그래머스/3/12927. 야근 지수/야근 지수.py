import heapq
def solution(n, works):
    answer = 0
    
    max_heap = [-work for work in works]
    heapq.heapify(max_heap)

    while n > 0 and max_heap:
        M = heapq.heappop(max_heap)  
        if M == 0:
            break 
        heapq.heappush(max_heap, M + 1) 
        n -= 1

    return sum(x**2 for x in max_heap)
