from collections import Counter
def solution(lottos, win_nums):
    check_lst = []
    lottos_cnt = Counter(lottos)
    zero = lottos_cnt[0]
    
    for i in range(6):
        if lottos[i] in win_nums:
            check_lst.append(lottos[i])
    
    if (2 <= len(check_lst)) and (len(check_lst) <= 6):
        min_rank = 6-len(check_lst)+1
    else:
        min_rank = 6
    
    
    if (2 <= len(check_lst)+zero) and (len(check_lst)+zero <= 6):
        max_rank = 6-len(check_lst)-zero+1
    else:
        max_rank = 6
    
    
    return [max_rank, min_rank]