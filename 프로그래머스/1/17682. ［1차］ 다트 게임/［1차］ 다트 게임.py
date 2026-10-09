def function(score, x):
    if x == "S":
        return score
    elif x == "D":
        return score ** 2
    else:  # "T"
        return score ** 3

def solution(dartResult):
    scores = []
    num = ""
    for c in dartResult:
        if c.isdigit():
            num += c                              # "1", "10" 모으기
        elif c in "SDT":
            scores.append(function(int(num), c))  # 숫자 완성 → 제곱해서 넣기
            num = ""
        elif c == "*":
            scores[-1] *= 2                       # 이번 점수 2배
            if len(scores) >= 2:
                scores[-2] *= 2                   # 전 점수도 2배
        else:  # "#"
            scores[-1] *= -1                      # 이번 점수 음수로
    return sum(scores)