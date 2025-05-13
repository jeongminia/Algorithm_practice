def solution(survey, choices):
    answer = ''
    score = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }

    for i in range(len(survey)):
        disagree, agree = survey[i][0], survey[i][1]
        choice = choices[i]

        if choice < 4:
            score[disagree] += 4 - choice
        elif choice > 4:
            score[agree] += choice - 4
        
    print(score)

    if score['R'] >= score['T']:
        answer += 'R'
    else:
        answer += 'T'

    if score['C'] >= score['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer