import sys

# 입력 처리
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
money = list(map(int, data[1:]))

temp = []

for i in money:
    #print(temp)
    if i != 0:
        temp.append(i)
    else:
        if len(temp) != 0:
            temp.pop()
        else:
            pass

if len(temp) != 0:
    print(sum(temp))
else:
    print(0)