def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    score = [0, 0, 0]

    for i, a in enumerate(answers):
        print(i, a)
        for p in range(3):
            if a == patterns[p][i % len(patterns[p])]:
                score[p] += 1
    print(score)

    best = max(score)
    lst = []
    for p in range(3):
        if score[p]==best:
            lst.append(p+1)
    return lst