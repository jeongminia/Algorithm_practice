def solution(s):
    s_lst = s.split(" ")
    int_lst = [int(i) for i in s_lst]
    
    a = min(int_lst)
    b = max(int_lst)
    
    answer = "{}".format(a) + " " + "{}".format(b)
    
    return answer