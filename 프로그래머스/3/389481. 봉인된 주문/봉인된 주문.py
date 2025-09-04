def convert_str_to_num(s: str) -> int:
    length = len(s)
    num = 0
    for j in range(length):
        num += (ord(s[j]) - 96) * (26 ** (length - 1 - j))
    return num


def convert_num_to_str(num: int) -> str:
    result = ""
    while num > 0:
        result = chr(((num - 1) % 26) + 97) + result
        num = (num - 1) // 26
    return result

def solution(n, bans):
    # bans를 숫자로 변환
    bans_nums = [convert_str_to_num(b) for b in bans]
    bans_nums.sort()
    
    # 금지 주문이 n보다 앞에 있으면 n을 뒤로 밀기
    for bn in bans_nums:
        if bn <= n:
            n += 1

    # 최종 n을 문자열로 변환
    return convert_num_to_str(n)