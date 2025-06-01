def solution(players, m, k): # m=3(수용인원), k=4(시간)
    temp = [1]*(24) # 증설된 서버의 수
    plus = [0]*(len(players)) # 증설 횟수
    
    for i in range(24):
        now = players[i]
        
        if i+k>24:
            limit=24
        else:
            limit=i+k
        
        if temp[i]*m==now:
            plus[i]=1
            for u in range(i,limit):
                temp[u] += plus[i]
                
        elif temp[i]*m < now:
            not_yet = (now - (temp[i])*m)
            if not_yet<0:
                not_yet*=(-1)

            plus[i] = (not_yet//m)+1
           # print(i, temp[i], plus[i])
            
            for u in range(i,limit):
                temp[u] += plus[i]
        
    print(temp)
    print(plus)
    
    return sum(plus)