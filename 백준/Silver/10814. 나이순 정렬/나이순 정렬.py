import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
information = []
for line in data[1:]:
    age, name = line.split()
    information.append((int(age), name))

information.sort(key=lambda x: x[0])  # 나이만 기준으로 정렬

for age, name in information:
    print(age, name)