def solution(n):
    n_lst = list(str(n))
    answer = [int(n_lst.pop()) for i in range(len(n_lst))]
    return answer