def solution(priorities, location):
    answer = 0
    process = [[p,i] for i, p in enumerate(priorities)]
    
    target = max(priorities)
    while True:
        current = process.pop(0)
        
        if current[0]!=target:
            process.append(current)
        else:
            if current[1]==location:
                answer+=1
                return answer
                break
            else:
                answer+=1
       # print(target, current, process)
        
        target = max([i for i, j in process]) 
    
    return answer