from collections import deque

def hide_and_seek(n, k):
    max_limit = 100001
    time = [float('inf')] * max_limit
    time[n] = 0

    dq = deque([n])

    while dq:
        x = dq.popleft()

        if x == k:
            return time[x]

        # 순간이동: 비용 0
        if 0 <= 2 * x < max_limit and time[2 * x] > time[x]:
            time[2 * x] = time[x]
            dq.appendleft(2 * x)

        # 걷기: 비용 1
        for nx in [x - 1, x + 1]:
            if 0 <= nx < max_limit and time[nx] > time[x] + 1:
                time[nx] = time[x] + 1
                dq.append(nx)

n, k = map(int, input().split())

if n >= k:
    print(n - k)
else:
    print(hide_and_seek(n, k))
