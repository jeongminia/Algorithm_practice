def solution(n, lost, reserve):
    students = [1] * n
    
    for r in reserve:
        students[r-1] += 1
    for l in lost:
        students[l-1] -= 1
        
    # 체육복 빌려주기 순회
    for i in range(n):
        if students[i] == 0: # 체육복이 없는 학생이라면
            # 왼쪽 학생(i-1)에게 먼저 빌려본다
            if i > 0 and students[i-1] == 2:
                students[i-1] -= 1
                students[i] += 1
            # 왼쪽 안 되면 오른쪽 학생(i+1)에게 빌려본다
            elif i < n-1 and students[i+1] == 2:
                students[i+1] -= 1
                students[i] += 1
                
    # 체육복이 1벌 이상인 학생 수 카운트
    return len([s for s in students if s >= 1])