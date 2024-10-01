def solution(t, p):
    answer = 0
    t_lst = []
    
    while True:
        t_lst.append(int(t[answer:answer+len(p)]))
        answer += 1
        if (answer+len(p)-1) == len(t) :
            break
            
    print(t_lst)
    
    check = 0
    for i in t_lst:
        if i <= int(p):
            check += 1
    
    return check