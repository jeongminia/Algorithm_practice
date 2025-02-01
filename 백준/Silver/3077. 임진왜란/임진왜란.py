import sys
from itertools import combinations
from collections import deque

input = sys.stdin.read
data = input().splitlines() 

N = int(data[0]) 
answer = data[1].split()  
hw = data[2].split() 

answer_index = {battle: idx for idx, battle in enumerate(answer)}

total_pairs = (N * (N - 1)) // 2
score = 0

for a, b in combinations(hw, 2):
    if answer_index[a] < answer_index[b]: 
        score += 1

print(str(score)+"/"+str(int((N*(N-1))/2)))