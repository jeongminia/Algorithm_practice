import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input())

col = []  # 각 줄의 통로 위치를 저장

for _ in range(N - 2):
    row = input().strip()
    for j in range(4):
        if row[j] == '0':
            col.append(j)
            break

result = INF

for target_col in range(4):  # 0~3번 열 중 어디로 통로를 맞출지
    total_rotation = 0
    for cur_col in col:
        diff = abs(cur_col - target_col)
        total_rotation += 1 if diff == 3 else diff  # 최소 회전 수 계산
    result = min(result, total_rotation)

# 초기 위치 (0,0) → 우측 끝 (0,3): 3칸
# 아래로 내려가는 이동: N-1칸
# 중간 줄 회전 횟수: result
print(3 + (N - 1) + result)
