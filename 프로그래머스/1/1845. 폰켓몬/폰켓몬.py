from collections import Counter

def solution(nums):
#    answer = 0
    n = len(nums)//2
    
   # print(Counter(nums).keys())
    
    if len(Counter(nums).keys()) <= n:
        return len(Counter(nums).keys())
    else:
        return n