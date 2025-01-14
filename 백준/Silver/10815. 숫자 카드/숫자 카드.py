import sys

input = sys.stdin.read
data = input().splitlines()

n, m = int(data[0]), int(data[2])

check_lst = set(list(map(int, data[1].split())))
temp = list(map(int, data[3].split()))

answer = []

for i in temp:
    if i in check_lst:
        answer.append("1")
    else:
        answer.append("0")

print(" ".join(answer))