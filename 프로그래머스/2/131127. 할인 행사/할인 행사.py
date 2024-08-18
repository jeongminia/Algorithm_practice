from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    dict_want = dict(zip(want, number))

    for i in range(len(discount) - 9):
        dis_lst = Counter(discount[i:i+10])
        
        if all(dis_lst[item] >= dict_want[item] for item in dict_want):
            answer += 1
    
    return answer
