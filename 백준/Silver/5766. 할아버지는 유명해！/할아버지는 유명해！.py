import sys
from collections import Counter

input = sys.stdin.read
data = [line for line in input().strip().split("\n") if line.strip()]

test_cases = []
index = 0

while index < len(data):
    n, m = map(int, data[index].split())
    if n == 0 and m == 0:  # 입력 종료 조건
        break
    rankings = []
    for i in range(1, n + 1):
        rankings.append(list(map(int, data[index + i].split())))
    test_cases.append(rankings)
    index += n + 1
    
for weekly_rankings in test_cases:
    points = {}
    for week in weekly_rankings:
        weekly_counter = Counter(week) 
        for player, count in weekly_counter.items():
            points[player] = points.get(player, 0) + count

    if len(points) < 2:
        print("")  # 2등이 없는 경우 빈 줄 출력
    else:
        # 2등 점수 구하기
        second_highest = sorted(points.items(), key=lambda x: -x[1])[1][1]
        second_players = [player for player, score in points.items() if score == second_highest]
        print(" ".join(map(str, sorted(second_players)))) 