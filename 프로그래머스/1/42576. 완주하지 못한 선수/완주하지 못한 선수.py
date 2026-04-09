from collections import Counter

def solution(participant, completion):
    answer = ''
    
    p_cnt = dict(Counter(participant))
    c_cnt = dict(Counter(completion))
    
    for p in c_cnt.keys():
        p_cnt[p] -= c_cnt[p]
        
  #  print(p_cnt)

    return [k for k, v in p_cnt.items() if v == 1][0]