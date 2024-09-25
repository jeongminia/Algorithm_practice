from collections import Counter

def solution(s):
    
    s_lst = {key: value for key, value in dict(Counter([k for k in s])).items() if value == 1}
    
    return ''.join(sorted(list(s_lst.keys())))