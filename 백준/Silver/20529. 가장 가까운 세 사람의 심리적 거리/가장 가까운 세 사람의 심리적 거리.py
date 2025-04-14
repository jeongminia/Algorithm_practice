from itertools import combinations

t = int(input())  
all_cases = []

for _ in range(t):
    n = int(input()) 
    mbtis = input().split() 
    all_cases.append(mbtis)

def cal_distance(person1, person2):
    sum = 0

    for i in range(4):
        if person1[i] != person2[i]:
            sum += 1

    return sum

for group in all_cases:
    if len(group) >= 33:
        print(0)
        continue  # 비둘기집 원리: 33명 이상이면 무조건 최소 거리 0

    min_total = float('inf')
    for a, b, c in combinations(group, 3):
        dist = cal_distance(a, b) + cal_distance(b, c) + cal_distance(a, c)
        min_total = min(min_total, dist)

        if min_total == 0:
            break  # 최소값 나왔으면 더 돌릴 필요 없음

    print(min_total)