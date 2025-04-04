import sys

input = sys.stdin.read
data = input().splitlines()

lst = list(map(int, data[1:]))

zero, minus, one, plus = 0, [], 0, []

for i in range(len(lst)):
    if lst[i] == 0:
        zero += 1
    elif lst[i] < 0:
        minus.append(lst[i])
    elif lst[i] == 1:
        one += 1
    else:
        plus.append(lst[i])

ans = 0
plus.sort(reverse=True)
minus.sort()

# 양수 처리기
if len(plus)%2==0:
    for i in range(0, len(plus), 2):
        ans += plus[i]*plus[i+1]
else:
    for i in range(0, len(plus)-1, 2):
        ans += plus[i]*plus[i+1]

    # 하나 남으면 더해버리기
    ans += plus[-1]

# 음수 처리기
if len(minus)%2==0:
    for i in range(0, len(minus), 2):
        ans += minus[i]*minus[i+1]
else:
    for i in range(0, len(minus)-1, 2):
        ans += minus[i]*minus[i+1]
        
    # 하나 남으면 없애버리기
    if zero == 0: 
        ans += minus[-1]

if one > 0:
    ans += one

print(ans)