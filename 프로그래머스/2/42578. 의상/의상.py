from collections import Counter
from math import *

def solution(clothes):
    cloth_lst = dict(Counter([clothes[i][1] for i in range(len(clothes))])).values()
    answer = prod([i+1 for i in cloth_lst])-1
    return answer
    