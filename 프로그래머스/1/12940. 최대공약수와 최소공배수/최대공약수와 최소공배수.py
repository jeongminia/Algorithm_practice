import math

def solution(n, m):
    answer = [math.gcd(n, m)]
    answer.append((n * m) // answer[0])
    return answer