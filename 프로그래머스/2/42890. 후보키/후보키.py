from itertools import combinations

def solution(relation):
    answer = 0
    r, c = len(relation), len(relation[0])
    c_lst = [i for i in range(c)]
    comb_lst = []
    
    for i in range(1, c+1):
        for j in combinations(c_lst, i):
            comb_lst.append(list(j))

    for_answer = []
    
    for i in comb_lst:
        # 최소성 검사: 이미 등록된 후보키의 부분집합이면 continue
        if any(set(a).issubset(set(i)) for a in for_answer):
            continue

        check = []
        for row in relation:
            key = tuple(row[t] for t in i)  # 튜플로 묶어서 hashable하게
            check.append(key)

        if len(set(check)) == r:
            for_answer.append(i)
            answer += 1

    return answer
