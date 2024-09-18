import heapq

def solution(operations):
    hq = []
    for operation in operations:
        if operation[0] == 'I':
            num = int(operation[2:]) # 숫자부터 들어가게, int 변환
            heapq.heappush(hq,num)
        elif operation == 'D 1':
            if hq:
                max_value = max(hq)
                hq.remove(max_value)
                heapq.heapify(hq)
        else:
            if hq:
                heapq.heappop(hq)
    
    if hq == []:
        return [0,0]
    else:
        return [max(hq), min(hq)]