def solution(scores):
    wanho = scores[0]
    scores.sort(key = lambda x : (-x[0], x[1])) # 근무태도 높은 순으로 정렬
    
    # print(scores)
    
    # 인센티브 수령 대상만! 확인하기 위해 동료 평가 값 확인
    max_att = 0
    new_lst = []
    for score in scores:
        if score[1] < max_att:
            if score == wanho:
                return -1
        else:   
            max_att = max(score[1], max_att)
            new_lst.append(score)
    
    # print(new_lst)
    
    sum_rank = 0
    insentive = [i[0] + i[1] for i in new_lst]
    
    for i in insentive:
        if i > wanho[0] + wanho[1]:
            sum_rank += 1
    
    return sum_rank+1