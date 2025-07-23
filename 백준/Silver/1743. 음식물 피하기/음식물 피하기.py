import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
visited = [[1] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    visited[x - 1][y - 1] = 0  # 쓰레기가 있는 위치를 0으로 표시

# BFS를 이용해 연결된 쓰레기 덩어리의 크기를 구함
def bfs(i, j):
    cnt = 1
    q = deque([(i, j)])
    visited[i][j] = 1  # 방문 표시

    while q:
        x, y = q.popleft()

        # 상하좌우 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if not ((0<=nx<n)and(0<=ny<m)):  # 범위를 벗어나면 패스
                continue
            if visited[nx][ny]:  # 쓰레기가 없으면 패스
                continue

            cnt += 1 # 영역 크기 증가
            visited[nx][ny] = 1  # 방문 표시
            q.append((nx, ny))

    return cnt

def solution(n, m, visited):
    trash = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]: # 해당 부분에 쓰레기가 있다면
                trash = max(bfs(i,j), trash)
    return trash

print(solution(n,m,visited))