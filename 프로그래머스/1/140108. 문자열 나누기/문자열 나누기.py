def solution(s):
    answer = 0
    x = s[0]
    x_cnt = 1
    notx_cnt = 0

    i = 1
    while i<len(s):
        if x_cnt != notx_cnt:
            if s[i] != x:
                notx_cnt+=1
            else:
                x_cnt+= 1
        else:
            answer +=1
            x = s[i]
            x_cnt = 1
            notx_cnt = 0
        
        i+=1

    #print(notx_cnt, x_cnt)

    
    return answer+1