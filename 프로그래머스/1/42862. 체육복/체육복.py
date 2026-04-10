def solution(n, lost, reserve):
    answer = 0
    
    # 각 학생마다 체육복 보유 수
    students = [1]*n
    for l in lost:
        students[l-1]-=1
    for r in reserve:
        students[r-1]+=1
    print(students)
    
    
    for i in range(n):
        if (students[i]==0):
            if i==0 and (students[i+1]==2):
                students[i+1]-=1
                students[i]+=1
            if i>0:
                if (i!=n-1) and (students[i-1]==2):
                        students[i-1]-=1
                        students[i]+=1
                elif (i!=n-1) and (students[i+1]==2):
                        students[i+1]-=1
                        students[i]+=1
                elif (i==n-1) and (students[i-1]==2):
                    students[i-1]-=1
                    students[i]+=1
    
    # 체육수업을 들을 수 있는 학생 수
    for a in students:
        if a>0:
            answer+=1
    return answer