import math

M, N = map(int, input().split())

answer = [math.gcd(M,N)]
answer.append(M*N//answer[0])

print(answer[0])
print(answer[1])