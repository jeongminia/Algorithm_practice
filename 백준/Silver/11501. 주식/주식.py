import sys

T = int(sys.stdin.readline())  # 테스트케이스 수

test_cases = []
for _ in range(T):
    N = int(sys.stdin.readline())  # 날짜 수
    prices = list(map(int, sys.stdin.readline().split()))  # 주가 리스트
    test_cases.append((N, prices))

for stock, day in test_cases:
    max_price = 0
    profit = 0
    for i in range(len(day)-1, -1, -1):
        #print(day[i])

        if max_price < day[i]:
            max_price = day[i]
        if max_price > day[i]:
            profit += max_price - day[i]

    print(profit)