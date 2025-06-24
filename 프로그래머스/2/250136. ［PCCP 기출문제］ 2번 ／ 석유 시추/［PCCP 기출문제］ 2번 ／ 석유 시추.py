def dfs(y, x, cid, visited, land, column_map, dy, dx, n, m):
    stack = [(y, x)]
    visited[y][x] = True
    count = 0

    while stack:
        cy, cx = stack.pop()
        count += 1
        column_map[cx].add(cid)

        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < n and 0 <= nx < m:
                if land[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    stack.append((ny, nx))
    
    return count

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False]*m for _ in range(n)]
    component_id = 0
    component_size = dict()
    column_map = [set() for _ in range(m)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and not visited[y][x]:
                component_id += 1
                size = dfs(y, x, component_id, visited, land, column_map, dy, dx, n, m)
                component_size[component_id] = size

    answer = 0
    for col in range(m):
        total = sum(component_size[cid] for cid in column_map[col])
        answer = max(answer, total)

    return answer
