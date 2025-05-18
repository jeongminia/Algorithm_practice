def can_clear_all_puzzles(level, diffs, times, limit):
    total_time = 0
    for i in range(len(diffs)):
        diff = diffs[i]
        time_cur = times[i]
        time_prev = times[i-1] if i > 0 else 0

        if level >= diff:
            total_time += time_cur
        else:
            mistakes = diff - level
            total_time += mistakes * (time_cur + time_prev) + time_cur

        if total_time > limit:
            return False  # 시간 초과 시 미리 종료
    return True

def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_clear_all_puzzles(mid, diffs, times, limit):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
