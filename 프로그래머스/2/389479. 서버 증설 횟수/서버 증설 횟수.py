def solution(players, m, k): # m=3(수용인원), k=4(시간)
    temp = [1]*(24) # 증설된 서버의 수
    plus = [0]*(24) # 증설 횟수
    
    for i in range(24):
        now = players[i]
        
        # out of range 방지를 위해 변수 선언
        limit = min(24, i+k)
        
        if temp[i]*m <= now:
            not_yet = (now - (temp[i])*m)
            if not_yet<0:
                not_yet*=(-1)

            plus[i] = (not_yet//m)+1
            for u in range(i, limit):
                temp[u] += plus[i]
                
    return sum(plus)