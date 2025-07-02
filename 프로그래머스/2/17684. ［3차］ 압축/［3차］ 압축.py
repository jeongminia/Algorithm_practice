def solution(msg):
    answer = []
    dictionary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    next_index = 27  # 다음 추가될 색인 번호
    i = 0

    while i < len(msg):
        w = msg[i]
        j = i + 1
        # 사전에 있는 가장 긴 문자열 w 찾기
        while j <= len(msg) and msg[i:j] in dictionary:
            w = msg[i:j]
            j += 1
        
        # 색인 번호 추가
        answer.append(dictionary.index(w) + 1)

        # 사전에 w + 다음 글자 추가
        if j <= len(msg):
            dictionary.append(msg[i:j])

        # 다음 탐색 위치 갱신
        i += len(w)
    
    return answer
