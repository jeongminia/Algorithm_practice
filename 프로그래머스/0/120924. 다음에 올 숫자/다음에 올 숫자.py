def solution(common):
    
    if common[0]-common[1] != common[1]-common[2]: # 등비수열
        r = common[1]/common[0]
        return common[-1]*r
    else: # 등차수열
        r = common[1]-common[0]
        return common[-1] + r
        