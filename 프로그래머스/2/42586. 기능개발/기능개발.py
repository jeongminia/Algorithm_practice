def solution(progresses, speeds):
    answer = []
    
    days=[]
    for i in range(len(speeds)):
        x=100-progresses[i]
        if x%speeds[i]!=0:
            days.append(x//speeds[i]+1)
        else:
            days.append(x//speeds[i])
   # print(answer) # 이게 바로 주식 급락이란 같은 원리인데..
    
    answer=[]
    base = days[0]
    cnt = 0 
    for x in days:
        if x <= base:
            cnt+=1
        else: #           x > base
            answer.append(cnt)
            base=x
            cnt=1
            
    answer.append(cnt)  
    return answer