N, D = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(N)]

# 거리 배열 초기화: 0부터 D까지 최소 거리
dp = [float('inf')] * (D + 1)
dp[0] = 0  # 시작점은 거리 0

for i in range(D + 1):
    # 1칸 전진 (기본 도로)
    if i + 1 <= D:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    # 지름길 확인
    for start, end, cost in path:
        if start == i and end <= D:
            dp[end] = min(dp[end], dp[start] + cost)

print(dp[D])



