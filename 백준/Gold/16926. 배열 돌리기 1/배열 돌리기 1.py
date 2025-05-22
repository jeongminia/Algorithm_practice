# 입력
N, M, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

# 방향: 좌 → 하 → 우 → 상 (반시계 방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 몇 개의 레이어를 돌려야 하나? => min(N, M) // 2
layers = min(N, M) // 2

for layer in range(layers):
    # 이 레이어의 사각형 테두리 모양 추출
    r1, c1 = layer, layer
    r2, c2 = N - 1 - layer, M - 1 - layer

    # 현재 테두리의 값을 순서대로 리스트에 저장
    q = []

    # 위
    for j in range(c1, c2): q.append(array[r1][j])
    # 오른쪽
    for i in range(r1, r2): q.append(array[i][c2])
    # 아래
    for j in range(c2, c1, -1): q.append(array[r2][j])
    # 왼쪽
    for i in range(r2, r1, -1): q.append(array[i][c1])

    # R번 회전
    rot = R % len(q)
    q = q[rot:] + q[:rot]  # 리스트 슬라이싱으로 회전

    # 회전된 결과를 다시 맵에 반영
    idx = 0
    for j in range(c1, c2): 
        array[r1][j] = q[idx]
        idx += 1
    for i in range(r1, r2): 
        array[i][c2] = q[idx]
        idx += 1
    for j in range(c2, c1, -1): 
        array[r2][j] = q[idx]
        idx += 1
    for i in range(r2, r1, -1): 
        array[i][c1] = q[idx]
        idx += 1

# 출력
for row in array:
    print(*row)
