import sys
M, N = map(int, sys.stdin.read().split())

def is_prime(num):
    if num < 2:  # 소수는 2 이상이어야 함
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

prime_lst = []

for i in range(M, N+1):
    if is_prime(i):
        prime_lst.append(i)

if prime_lst:  # 소수가 있을 경우
    print(sum(prime_lst))
    print(min(prime_lst))
else:  # 소수가 없을 경우
    print(-1)