import sys
from collections import Counter
import math

# 입력 처리
input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
data = list(map(int, data[1:]))

# 1. 산술평균
mean = sum(data) / n
print(math.floor(mean + 0.5) if mean >= 0 else math.ceil(mean - 0.5))

# 2. 중앙값
data.sort()
print(data[n // 2])

# 3. 최빈값
counter = Counter(data)
most_common = counter.most_common()
max_freq = most_common[0][1]  # 최빈값 빈도수
freq_values = [num for num, freq in most_common if freq == max_freq]
freq_values.sort()

if len(freq_values) == 1:  # 최빈값이 하나뿐이면 그대로 출력
    print(freq_values[0])
else:  # 여러 개의 최빈값이 있다면 두 번째로 작은 값 출력
    print(freq_values[1])

# 4. 범위
print(max(data) - min(data))
