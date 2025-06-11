def solution(s):
    if len(s) == 1:
        return 1  # 길이 1인 예외 처리

    answer = len(s)  # 압축 안 했을 때 기본값
    
    window_size = 1

    while window_size <= (len(s) // 2):  # <= 로 수정해야 마지막 길이 포함
        prev = s[0:window_size]
        count = 1
        temp = 0  # 압축 결과의 길이

        for i in range(window_size, len(s), window_size):
            cur = s[i:i + window_size]
            if cur == prev:
                count += 1
            else:
                temp += len(prev) + (len(str(count)) if count > 1 else 0)
                prev = cur
                count = 1

        # 마지막 덩어리 처리
        temp += len(prev) + (len(str(count)) if count > 1 else 0)

        answer = min(answer, temp)
        window_size += 1

    return answer
