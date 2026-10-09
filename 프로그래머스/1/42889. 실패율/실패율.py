from collections import Counter

def solution(N, stages):
    answer = []
    
    cnt_st = sorted(dict(Counter(stages)).items()) # [스테이지: 해당 스테이지에서 탈락한 사람]
    
    users = len(stages)
    y = 1
    for i in range(1, N+1):
        this_stage = i
        if cnt_st and  cnt_st[0][0] == i: # 현재 스테이지에서 탈락한 사람 찾아내기
            x = cnt_st[0][1]/users
            answer.append([x, y])
            
            users-= cnt_st[0][1]
            cnt_st.pop(0)
            
        else: # 현재 스테이지에서  탈락한 사람 없음
            answer.append([0,y])
        y+=1
        
    #print(answer)
    
    answer.sort(key = lambda x: -x[0])
    #print(answer)        
    return [i[1] for i in answer]