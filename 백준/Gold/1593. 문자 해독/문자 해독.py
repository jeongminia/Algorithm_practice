import sys
from collections import Counter

input = sys.stdin.read
data = input().splitlines()

len_w, len_s = map(int, data[0].split())
W = data[1].strip()
S = data[2].strip()
cnt = 0

w_cnt = Counter(W)
window = Counter(S[:len_w])

if window == w_cnt:
    cnt += 1

for i in range(len_w, len_s):
    # 윈도우 슬라이딩: 왼쪽 제거, 오른쪽 추가
    left_char = S[i - len_w]
    new_char = S[i]

    window[left_char] -= 1
    if window[left_char] == 0:
        del window[left_char]  # 꼭 삭제해야 dict 비교에서 성능 좋아짐

    window[new_char] += 1

    if window == w_cnt:
        cnt += 1

print(cnt)