def solution(array):
    array.sort()
    j = int(len(array) / 2)
    return array[j]