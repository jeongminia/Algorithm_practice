def dfs(node, visited, graph):
    visited[node] = True
    count = 1
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(neighbor, visited, graph) 
    return count

def solution(n, wires):
    answer = float('inf') # 비교하는 값이 처음에 어떤 값이 나오든 그 값으로 최소값이 갱신
    
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        visited = [False] * (n + 1)  
        graph[a].remove(b)
        graph[b].remove(a)
        
        network_size = dfs(a, visited, graph)
        other_network_size = n - network_size 
        
        answer = min(answer, abs(network_size - other_network_size))
        
        # 다시 전선 복구
        graph[a].append(b)
        graph[b].append(a)
    
    return answer