import math

def solution(numer1, denom1, numer2, denom2):
    # 분모의 최소공배수 구하기
    lcm = (denom1 * denom2) // math.gcd(denom1, denom2)

    # 분자 변환 후 더하기
    new_numer = numer1 * (lcm // denom1) + numer2 * (lcm // denom2)

    # 기약분수로 만들기
    gcd = math.gcd(new_numer, lcm)
    return [new_numer // gcd, lcm // gcd]