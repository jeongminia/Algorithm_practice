def solution(numbers):
    add = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            a = numbers[i] + numbers[j]
            add.append(a)
            
    answer = sorted(list(set(add)))
    
    return answer