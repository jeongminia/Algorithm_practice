from collections import deque
n = int(input()) # 체스판 크기
a, b, c, d = map(int, input().split())
start = [a, b]
goal = [c, d]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

# start에서 goal로 이동하는 최소 횟수

def bfs(start):
    q = deque([start])
    visited = [[0]*n for _ in range(n)] # 격자만큼 시작
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = visited[x][y] + True
                q.append([nx, ny])

    return visited

result = bfs(start)
print(result[goal[0]][goal[1]]-1)

