from collections import deque

def solution(N, K):
    dq = deque(range(1, N + 1))  # 청설모 번호만 저장

    while len(dq) > 1:
        if len(dq) >= K:
            # 첫 번째 청설모는 제외하고 K-1마리 제거
            survivor = dq.popleft()
            for _ in range(K - 1):
                dq.popleft()
            dq.append(survivor)  # 살아남은 청설모를 맨 뒤로 추가
        else:
            # 남은 청설모가 K보다 적으면 첫 번째 제외하고 다 제거
            dq = deque([dq[0]])

    return dq[0]

# 입력 및 실행
N, K = map(int, input().split())
print(solution(N, K))
