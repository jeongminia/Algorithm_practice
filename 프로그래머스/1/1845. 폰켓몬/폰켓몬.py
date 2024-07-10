from collections import Counter
def solution(nums):
    k = len(nums)/2
    
    if len(Counter(nums)) >= k:
        answer = k
    else:
        answer = len(Counter(nums))

    return answer