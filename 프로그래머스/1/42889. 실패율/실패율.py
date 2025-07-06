from collections import Counter

def solution(N, stages):
    answer = []
    
    stages.sort()
    stages_cnt = dict(Counter(stages))
 #   print(stages_cnt)
    
    i=1 # initial stage
    while N:
        if i not in stages_cnt.keys():
            percentage = 0
        else:
            percentage = stages_cnt[i]/sum(stages_cnt.values())
            stages_cnt.pop(i)
        
     #   print(i, percentage)
        answer.append([i,percentage])
        i+=1
        N-=1
    
    answer.sort(key=lambda x:-x[1])
    
    return [a[0] for a in answer]