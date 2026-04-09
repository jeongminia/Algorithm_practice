from collections import Counter
def solution(clothes):
    closet = Counter([item[1] for item in clothes])
    answer = 1
    for i in list(closet.values()):
        answer*=(i+1)
    return answer-1