import sys
sys.setrecursionlimit(10**6) # 깊이 제한 

input = sys.stdin.read
data = input().strip().splitlines()

N, M = map(int, data[0].split())
graph = {i: [] for i in range(1, N+1)}  # 모든 노드 초기화 (빈 리스트 포함)

if M > 0:
    for i in range(1, M + 1):  
        a, b = map(int, data[i].split())
        graph[a].append(b)
        graph[b].append(a) 

visited = {node: False for node in range(1, N+1)} 
def dfs(v):    
    visited[v] = True  
    for neighbor in graph[v]:  
        if not visited[neighbor]: 
            dfs(neighbor)

cnt = 0  
for node in range(1, N+1):
    if not visited[node]:  
        dfs(node)
        cnt += 1  

print(cnt)
