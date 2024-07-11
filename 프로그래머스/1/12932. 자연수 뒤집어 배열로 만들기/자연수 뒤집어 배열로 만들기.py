def solution(n):
    n_lst = list(str(n))
    answer = []
    
    for i in range(len(n_lst)):
        answer.append(int(n_lst.pop()))
    return answer