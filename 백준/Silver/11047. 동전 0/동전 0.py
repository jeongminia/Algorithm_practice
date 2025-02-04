# 가장 큰 동전부터 채우면 최적해 보장
import sys

input_data = sys.stdin.read().splitlines()
N, K = map(int, input_data[0].split())
coins = [int(input_data[i]) for i in range(1, N+1)]

i = len(coins)
answer = 0

while i != 0:
    i -= 1
    target = coins[i]
    if K >= target:
        cnt = K // target
        answer += cnt
        #print('몫', cnt)
        K -= cnt * target

    if K == 0:
        break


print(answer)