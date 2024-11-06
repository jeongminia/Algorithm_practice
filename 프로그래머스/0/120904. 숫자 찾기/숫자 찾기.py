def solution(num, k):
    num = [i for i in str(num)]
    
    if str(k) in num:
        return num.index(str(k)) + 1
    else:
        return -1