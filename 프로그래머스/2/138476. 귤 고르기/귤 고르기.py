from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    cnt = Counter(tangerine)
   # print(cnt)
    temp = sorted(list(cnt.values()),reverse=True)
    for i in temp:
        #print(k, i)
        if k-i <= 0:
            k-=i
            answer+=1
            break
        else:
            k-=i
            answer+=1
        
    
    return answer