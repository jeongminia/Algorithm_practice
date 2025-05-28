import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    INF = int(1e9)
    graph = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        graph[i][i] = 0
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    answer = 0
    for v in range(1, N+1):
        # v 번 노드가 순위가 정해져있는지 확인
        for i in range(1, N+1):
            if graph[i][v] < INF or graph[v][i] < INF:
                continue
            else:
                break
        else: # 위 for 문을 다 돌았다면
            answer += 1
    print(answer)

if __name__ == "__main__":
    solution()