from collections import Counter

def solution(X, Y):
    counterX = Counter(X)
    counterY = Counter(Y)
    
    result = []

    # 9부터 0까지 숫자 확인
    for digit in map(str, range(9, -1, -1)):
        count = min(counterX[digit], counterY[digit])
        result.extend([digit] * count)

    if not result:
        return "-1"
    if result[0] == '0':
        return "0"
    return ''.join(result)
