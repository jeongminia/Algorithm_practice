n, M, v = map(int, input().split())
m = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)
for i in range(M):
    a, b = map(int, input().split())
    m[a][b] = m[b][a] = 1

#dfs
def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    #재귀 함수 선어 (v와 인접한 곳을 찾고 방문하지 않았다면 시행)
    for i in range(1, n+1):
        if visited[i] == 0 and m[v][i] ==1:
            dfs(i)

def bfs(v):
    #방문해야할 곳을 순서대로 넣을 큐
    queue = [v]


    #dfs를 완료한 visited배열(1로 되어있음)에서 0으로 방문 체크
    visited[v] = 0

    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] == 1 and m[v][i] == 1:
                queue.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)