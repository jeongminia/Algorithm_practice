def solution(price, money, count):
    answer = -1
    
    
    if sum([price*(i+1) for i in range(count)]) - money > 0:
        return sum([price*(i+1) for i in range(count)]) - money
    else:
        return 0
