from collections import Counter
def solution(nums):

    M=len(nums)//2
    
    cnt=Counter(nums)
    print(cnt, )
    
    if len(cnt) >= M:
        return M
    else:
        return len(cnt)