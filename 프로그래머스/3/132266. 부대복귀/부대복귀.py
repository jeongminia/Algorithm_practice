from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = [-1] * (n + 1)
    dist[destination] = 0
    q = deque([destination])

    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                q.append(neighbor)

    return [dist[s] for s in sources]
