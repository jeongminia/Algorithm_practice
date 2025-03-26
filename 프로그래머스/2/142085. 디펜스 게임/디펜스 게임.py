import heapq

def solution(n, k, enemy):
    total_sum = 0
    max_enemy = []

    for i, e in enumerate(enemy):
            total_sum += e
            heapq.heappush(max_enemy, -e) 
           # print('heap을 보여줘', max_enemy)

            if total_sum > n:
           #     print('---------', total_sum, n)
                if k > 0:
                    total_sum += heapq.heappop(max_enemy)  
                    k -= 1
                else:
                    return i  # 더 이상 못 막음
    return len(enemy)