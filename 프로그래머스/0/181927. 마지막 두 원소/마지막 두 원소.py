def solution(num_list):
    
    k = num_list[-1] - num_list[-2]
    
    if k > 0:
        num_list.append(k)
    else:
        k = num_list[-1] * (2)
        num_list.append(k)
    
    return num_list