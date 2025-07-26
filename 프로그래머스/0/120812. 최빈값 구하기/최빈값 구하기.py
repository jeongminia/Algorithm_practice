from collections import Counter
def solution(array):
    answer = 0
    
    temp = 0
    for key, value in Counter(array).items():
        if temp < value:
            answer = key
            temp = value
        elif temp == value:
            answer = -1
            temp = value 
    #    print(key, value, temp, answer)
    
    return answer