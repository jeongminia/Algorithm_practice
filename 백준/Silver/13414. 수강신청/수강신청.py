import sys
input = sys.stdin.readline

k, l = map(int, input().split())
students = [input().strip() for _ in range(l)]

# 인덱스 기준으로 설정해서 마지막 신청만 남김
student_dict = {}
for idx, student in enumerate(students):
    student_dict[student] = idx 

# 학생 신청 순서대로 정렬(인덱스 순서로)
sorted_students = sorted(student_dict.items(), key=lambda x: x[1])

# 선착순 k명 출력
for i in range(min(k, len(sorted_students))):
    print(sorted_students[i][0])