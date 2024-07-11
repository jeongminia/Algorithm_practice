from collections import deque
def solution(arr):
    arr = deque(arr)
    answer = [arr.popleft()]
    
    for i in range(0, len(arr)):
        a = arr.popleft()
        if answer[len(answer)-1] != a:
            answer.append(a)    

    return answer