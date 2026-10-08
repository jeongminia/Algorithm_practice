def solution(arr):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        elif (i in answer) and (i != answer[-1]):
       #     print(i, answer[-1])
            answer.append(i)
        
    return answer