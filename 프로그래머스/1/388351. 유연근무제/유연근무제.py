# 오늘부터 일주일 동안 각자 설정한 출근 희망 시각에 늦지 않고 출근한 직원들에게 상품을 주는 이벤트를 진행
def solution(schedules, timelogs, startday):
    answer = 0

    event_days = 0
    for i in range(len(timelogs[0])):
        if (startday+i)%7 not in [0, 6]:
            event_days += 1
            
    for i in range(len(timelogs)):
        person = timelogs[i]
        right = event_days
        
        time = schedules[i] + 10 
        if time%100 >= 60:
          time = (time//100 + 1)*100 + (time%100 - 60)
        
        
        for j in range(len(person)): 
            # 주말이 아니여야 함
            if (startday+j)%7 not in [0, 6]:
                if (person[j] <= time):
                    right -= 1
                else:
                    break
                    
        if right == 0:
            answer += 1

    return answer
    