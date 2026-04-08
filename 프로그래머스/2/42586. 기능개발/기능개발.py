def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] != 0:
            k = (100-progresses[i])//speeds[i] + 1
        else:
            k = (100-progresses[i])//speeds[i]
        days.append(k)
#    print(days)
  #  for j in range(1,len(days)):
    for j in days:
        if answer == []:
            answer.append(1)
            max_days = j
        else:        
            if j <= max_days:
                answer[-1]+=1
            else:
                answer.append(1)
                max_days = j
       # print(j, max_days, answer)
    
    return answer # 각 배포마다 몇 개의 기능이 배포되는지