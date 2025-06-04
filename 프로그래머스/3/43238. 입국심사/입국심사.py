def solution(n, times):
    answer = 0 # 해당 시간
    
    # 최적의 시간 찾기(시간 감소하며)
    left, right = min(times), max(times)*n
    
    # 중간 값이 n명을 심사 할 수 있는 시간인지 확인하며 이분 탐색을 진행
    while left <= right:
        mid = (left+ right)//2
        checked = 0 # 모든 심사관들이 mid분 동안 심사한 사람의 수
        
        for time in times:
            checked += mid//time
            
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 break
            if checked >= n:
                break
        
        # pointer 위치 갱신
        if checked >= n: # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
            answer = mid
            right = mid - 1
      #      print(f"가능 ({checked} >= {n}), answer = {answer}, 새로운 right = {right}")
        else: # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
            left = mid + 1
      #      print(f"불가능 ({checked} < {n}), 새로운 left = {left}")
    
    return answer