def solution(left, right):
    cnt_lst = []
    answer = 0
    num = [i for i in range(left, right+1)]
    
    for k in num:
        cnt = 0 
        for j in range(1, k+1):
            if k % j == 0:
                cnt += 1
        cnt_lst.append(cnt)
    
    for i in range(len(cnt_lst)):
        if cnt_lst[i] % 2 == 0:
            answer += num[i]
        else:
            answer -= num[i]
            
    
    return answer