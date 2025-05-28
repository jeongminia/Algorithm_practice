from collections import deque

def solution(tickets):
    tickets.sort()  # 사전순 우선 탐색을 위한 정렬
    n = len(tickets)
    queue = deque()
    queue.append(("ICN", ["ICN"], [False] * n))  # 현재 위치, 경로, 사용 여부

    while queue:
        curr, path, used = queue.popleft()

        # 모든 티켓 사용 완료
        if len(path) == n + 1:
            return path

        for i in range(n):
            src, dst = tickets[i]
            if not used[i] and src == curr:
                new_used = used[:]  # 사용 상태 복사
                new_used[i] = True
                queue.append((dst, path + [dst], new_used))
