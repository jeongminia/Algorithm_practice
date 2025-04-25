def solution(gems):
    kind = len(set(gems))  # 필요한 보석 종류 수
    gem_counter = {}
    answer = [0, len(gems)]
    
    start = 0

    # 길이 기준으로 탐색
    for end in range(len(gems)):
        gem = gems[end]
        gem_counter[gem] = gem_counter.get(gem, 0) + 1
        
        # 윈도우가 모든 종류의 보석을 포함하면 start를 앞으로 줄일 수 있는지 확인
        while len(gem_counter) == kind:
            # 최소 구간 갱신
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            
            # 갱신이 안되면 start 위치 보석 하나 줄이기
            gem_counter[gems[start]] -= 1
            if gem_counter[gems[start]] == 0:
                del gem_counter[gems[start]]
            start += 1
            
    return [answer[0]+1, answer[1]+1] 