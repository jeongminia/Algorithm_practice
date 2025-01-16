import sys

input = sys.stdin.read
data = input().split()

def find_num(num):
    if num < 2:  # 소수는 2 이상이어야 함
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for num in range(int(data[0]),int(data[1])+1):
    if find_num(num) == True:
        print(num)