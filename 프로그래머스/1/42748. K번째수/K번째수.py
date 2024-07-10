def solution(array, commands):
    answer = []
    for arr in commands:
        com_arr = sorted(array[arr[0]-1:arr[1]])
        answer.append(com_arr[arr[2]-1])
    return answer