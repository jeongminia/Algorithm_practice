def convert(n, k):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if n == 0:
        return '0'
    else:
        result = ''
        while n > 0:
            result = digits[n % k] + result
            n //= k
        return result

def solution(n):
    ternary_reversed = convert(n, 3)[::-1]  # 3진법 변환 후 뒤집기
    return int(ternary_reversed, 3)         # 다시 10진수로 변환
