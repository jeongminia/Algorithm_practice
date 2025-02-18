def solution(name):
    spell_move = 0
    cursor_move = len(name) - 1 
    
    alphabet_list = [chr(i).upper() for i in range(ord('a'), ord('z') + 1)]

    for i, char in enumerate(name):
        if char != 'A':  
            spell_move += min(alphabet_list.index(char), len(alphabet_list) - alphabet_list.index(char))

        # 'A' 연속 구간 체크
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        
        # 최소 이동 거리 계산
        cursor_move = min(
            cursor_move, 
            2 * i + len(name) - next_i,  # 되돌아갔다가 가는 경우
            i + 2 * (len(name) - next_i)  # 우측 끝부터 다시 되돌아가는 경우
        )

    return spell_move + cursor_move

