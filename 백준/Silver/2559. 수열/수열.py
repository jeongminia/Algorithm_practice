import sys

input = sys.stdin.read
data = input().splitlines()
n, k = map(int, data[0].split())
temperatures = list(map(int, data[1].split()))

current_sum = sum(temperatures[:k])  
max_sum = current_sum 

# 슬라이딩 윈도우를 통해 최대 구간 합 계산
for i in range(k, n):
    current_sum += temperatures[i] - temperatures[i - k]
    max_sum = max(max_sum, current_sum)

print(max_sum)