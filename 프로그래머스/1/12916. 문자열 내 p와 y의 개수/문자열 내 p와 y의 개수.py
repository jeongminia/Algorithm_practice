def solution(s):
    cnt_p = 0 
    cnt_y = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] == 'p':
            cnt_p += 1
        elif s[i] == 'y':
            cnt_y += 1
    return cnt_p == cnt_y
    