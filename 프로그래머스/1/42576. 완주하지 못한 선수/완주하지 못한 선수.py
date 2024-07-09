from collections import Counter

def solution(participant, completion):
    
    # 이름, 수 기준으로 딕셔너리 생성
    part_cnt = dict(Counter(participant))
    
    # 다 진행해서 수가 0이 아닌 것을 출력
    for i in range(len(completion)):
        # completion에 있을 때마다 수를 -1
        a = completion.pop()
        part_cnt[a] = part_cnt[a] - 1 
        
    for key, value in part_cnt.items():
        if value > 0:
            answer = key
    return answer