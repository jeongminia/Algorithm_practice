submit = []

while True:
    try:
        line = input()
        if not line.strip():  # 빈 줄 입력 시 종료
            break
        submit.append(int(line))  # 정수로 변환하여 추가
    except EOFError:  
        break

submit.sort()

real_students = [i+1 for i in range(30)]
for i in range(len(real_students)):
  if real_students[i] not in submit:
    print(real_students[i])