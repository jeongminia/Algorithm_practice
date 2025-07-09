def solution(n, m, section):
    answer = 0
    wall = [1] * n  # 칠해진 상태
    for i in section:
        wall[i - 1] = 0
    j = 0     
    while j < n:
        if wall[j] == 0:
            answer += 1
            # j부터 m칸 칠함
            for k in range(j, min(j + m, n)):
                wall[k] = 1  # 덧칠 처리
            j += m  # 다음 위치는 m칸 뒤
        else:
            j += 1
            
    return answer