N, B = input().split()
B = int(B)

def char_to_val(c):
    if c.isdigit():
        return int(c)
    return ord(c.upper()) - ord('A') + 10  # 'A' → 10, 'Z' → 35

def convert(N: str, B: int) -> int:
    result = 0
    for i in N:
        result = result * B + char_to_val(i)
    return result

print(convert(N, B))