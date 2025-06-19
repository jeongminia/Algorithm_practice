def solution(cards):
    visited = [False] * len(cards)
    group_sizes = []

    for i in range(len(cards)):
        if not visited[i]:
            cnt = 0
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cur = cards[cur] - 1  # 다음 상자 index
                cnt += 1
            group_sizes.append(cnt)

    # 가장 큰 두 그룹 크기만 곱해서 반환
    if len(group_sizes) < 2:
        return 0
    group_sizes.sort(reverse=True)
    return group_sizes[0] * group_sizes[1]