import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
numbers = list(map(int, data[1].split()))
queries = [tuple(map(int, line.split())) for line in data[2:]]

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i-1] + numbers[i-1]

for s, e in queries:
    print(prefix_sum[e] - prefix_sum[s-1])