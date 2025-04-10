import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, graph))  # 가장 높은 지형의 높이

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, visited, rain_height):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx] and graph[ny][nx] > rain_height:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

max_safe_zone = 0

for rain in range(0, max_height + 1):
    visited = [[False]*n for _ in range(n)]
    safe_zone_count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > rain:
                bfs(j, i, visited, rain)
                safe_zone_count += 1

    max_safe_zone = max(max_safe_zone, safe_zone_count)

print(max_safe_zone)
