def solution(answers):
    give_up1 = [1,2,3,4,5]
    give_up2 = [2, 1, 2, 3, 2, 4, 2, 5]
    give_up3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    correct_1, correct_2, correct_3 = 0, 0, 0
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == give_up1[i%len(give_up1)]:
            correct_1 += 1
        if answers[i] == give_up2[i%len(give_up2)]:
            correct_2 += 1
        if answers[i] == give_up3[i%len(give_up3)]:
            correct_3 += 1
    
    a = max([correct_1, correct_2, correct_3])
    
    if a == correct_1:
        answer.append(1)
    if a == correct_2:
        answer.append(2)
    if a == correct_3:
        answer.append(3)

    return sorted(answer)