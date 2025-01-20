import sys

input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = list(map(int, data[1:]))

def find_num(num):
    if num < 2:  # 소수는 2 이상이어야 함
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for num in test_cases:
    while not find_num(num): 
        num += 1
    print(num)