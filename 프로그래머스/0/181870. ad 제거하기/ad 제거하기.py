def solution(strArr):
    result = []
    
    for j in strArr:
        if 'ad' not in j:
            result.append(j)
    
    return result