import sys
from collections import Counter

# 입력 받기
input = sys.stdin.read
data = input().splitlines()
N, M = map(int, data[0].split())

# 길이가 M 이상인 단어만 선택
words = [word for word in data[1:] if len(word) >= M]

# 단어 빈도수 계산
word_dict = Counter(words).items()

# 정렬: (빈도 내림차순, 길이 내림차순, 사전순 오름차순)
sorted_words = sorted(word_dict, key=lambda x: (-x[1], -len(x[0]), x[0]))

# 단어만 출력
for word, _ in sorted_words:
    print(word)
