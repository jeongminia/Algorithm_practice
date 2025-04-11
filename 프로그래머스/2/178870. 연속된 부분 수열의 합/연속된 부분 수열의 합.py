def solution(sequence, k):
    left, right = 0, 0
    sum_part = sequence[0]
    answer = [0, len(sequence)]  # 최소 구간 저장

    while right < len(sequence):
        if sum_part == k:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]

        if sum_part >= k:
            sum_part -= sequence[left]
            left += 1
        else:
            right += 1
            if right < len(sequence):
                sum_part += sequence[right]

    return answer
