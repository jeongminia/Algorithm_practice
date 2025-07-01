from collections import deque
# 현재 컨베이어 벨트의 상자 번호(rules) 기준으로 순회
def solution(order):
    answer = 0
    rules = deque(range(1, len(order) + 1))  # 컨베이어 벨트
    temp = []                                # 보조 벨트
    order = deque(order)                     # pop(0) 방지용

    while rules or temp:
        # 우선 현재 벨트 상자 확인
        if rules and rules[0] == order[0]:
            rules.popleft()
            order.popleft()
            answer += 1

        # 다음으로 보조 벨트 확인
        elif temp and temp[-1] == order[0]:
            temp.pop()
            order.popleft()
            answer += 1

        # 컨베이어에서 꺼내서 보조로 이동
        elif rules:
            temp.append(rules.popleft())

        # 어느 것도 맞지 않으면 종료
        else:
            break

    return answer # 실을 수 있는 상자의 개수