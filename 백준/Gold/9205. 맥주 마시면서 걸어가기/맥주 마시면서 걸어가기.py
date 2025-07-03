import sys
from collections import deque

def bfs(v, routes, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        curr = queue.popleft()
        for next_node in routes[curr]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    return visited

def solution(n, points):
    visited = [False]*len(points)
    routes = [[] for _ in range(len(points))]

    # 모든 쌍에 대해 연결 여부 판단
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            x1, y1 = points[i]
            x2, y2 = points[j]

            # 맥주를 다 마실 수 있으면 두 노드는 연결 가능함
            if abs(x1 - x2) + abs(y1 - y2) <= 1000:
                routes[i].append(j)
    #print(routes)

    visited = bfs(0, routes, visited)
    #print(visited)

    return 'happy' if visited[-1] else 'sad'

t = int(sys.stdin.readline()) # test case 개수
for _ in range(t):
    n = int(sys.stdin.readline())
    points = []
    for _ in range(n + 2):  # 집 + 편의점 n개 + 페스티벌 = 총 n+2개
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
    
    print(solution(n, points)) 

