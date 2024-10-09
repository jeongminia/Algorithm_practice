import sys
from collections import Counter

# 첫 번째 줄에서 입력받는 파일의 개수
n = int(input())

# 파일 이름들을 저장할 리스트
file_names = []

# n개의 파일 이름을 입력받음
for _ in range(n):
    file_name = sys.stdin.readline().strip()
    file_names.append(file_name)

file_types = [i.split('.')[1] for i in file_names]
file_dict = sorted(dict(Counter(file_types)).items(), key=lambda x: x[0], reverse=False)

for i in file_dict:
    print(i[0], i[1])