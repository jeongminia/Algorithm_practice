from itertools import combinations

# 첫 줄에 N과 M 입력
N, M = map(int, input().split())

# N개의 줄에 각 회원의 치킨 선호도 입력
preferences = []
for _ in range(N):
    preferences.append(list(map(int, input().split())))

max_satisfaction = 0

for combo in combinations(range(M), 3): 
    satisfaction = sum(max(preferences[i][j] for j in combo) for i in range(len(preferences)))
    max_satisfaction = max(max_satisfaction, satisfaction)

print(max_satisfaction)
