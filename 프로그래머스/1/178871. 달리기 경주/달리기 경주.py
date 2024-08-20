def solution(players, callings):
    # 선수의 이름을 키로, 인덱스를 값으로 가지는 딕셔너리 생성
    player_indices = {player: index for index, player in enumerate(players)}
    
    for call in callings:
        # 호출된 선수의 현재 인덱스
        current_index = player_indices[call]
        
        if current_index > 0:
            # 앞 선수와 자리 교환
            previous_player = players[current_index - 1]
            
            # 리스트에서 자리 바꿈
            players[current_index], players[current_index - 1] = players[current_index - 1], players[current_index]
            
            # 딕셔너리에서 인덱스 업데이트
            player_indices[call] = current_index - 1
            player_indices[previous_player] = current_index
    
    return players
