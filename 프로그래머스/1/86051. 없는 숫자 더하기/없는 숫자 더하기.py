def solution(numbers):
    num_lst = [i for i in range(10)]
    
    for j in sorted(numbers):
        num_lst.remove(j)
    
    return sum(num_lst)