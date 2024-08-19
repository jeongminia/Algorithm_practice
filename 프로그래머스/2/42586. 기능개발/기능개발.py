def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range(len(speeds)):
        n = round((100 - progresses[i])/speeds[i], 2)
        days.append(int(n) if n == int(n) else int(n) + 1)
    
    while days:
        current_day = days.pop(0)
        print(current_day)
        count = 1
        
        # 같은 배포일에 배포할 기능들 묶기
        while days and days[0] <= current_day:
        #    print(current_day, '>')
        #    print(days[0])
            days.pop(0)
            count += 1
        answer.append(count)
    return answer