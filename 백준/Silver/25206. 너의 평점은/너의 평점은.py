data = []
for _ in range(20):
    line = input().strip().split()
    data.append(line)

grade_to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

# 총 학점과 평점 합 계산
total = 0.0
credit_total = 0.0

for line in data:
    subject, credit, grade = line[0], float(line[1]), line[2]
    if grade == 'P':  # P 과목은 완전히 제외
        continue
    if grade in grade_to_score:  # F 포함 평점 변환
        score = grade_to_score[grade]
        total += credit * score
        credit_total += credit

if credit_total == 0:
    print(0.0)  # 학점이 없는 경우
else:
    print(total / credit_total)
