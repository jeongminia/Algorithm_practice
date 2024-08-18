def solution(s):
    # 문자열의 길이가 4 또는 6인지 확인
    if len(s) != 4 and len(s) != 6:
        return False
    
    k = sorted(s)[-1]
    
    if not k.isdigit():
        return False
    else:
        return True