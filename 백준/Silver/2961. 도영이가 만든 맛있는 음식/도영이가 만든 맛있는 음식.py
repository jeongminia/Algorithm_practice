import sys
from itertools import combinations

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
ingredients = [tuple(map(int, line.split())) for line in data[1:N+1]]

answer = float('inf')  
j = 1

while j != N+1:  
    for taste in combinations(ingredients, j):
        if len(taste) == 1:  
            sour = taste[0][0]
            bitter = taste[0][1]
        else:
            sour, bitter = 1, 0
            for i in taste:
                sour *= i[0]  
                bitter += i[1]  

        new = abs(sour - bitter)
        if new < answer:
            answer = new 

    j += 1  
    
print(answer)
