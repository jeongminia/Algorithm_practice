import sys
A, B = map(str, sys.stdin.read().split())

len_A = len(A)
answer = float('inf')

while len(B) != len_A - 1:

    check = B[:len_A]
    #print(check)
    cnt = 0

    for i in range(len_A):
        if check[i] != A[i]:
            cnt += 1
    #print(cnt)

    answer = min(answer, cnt)
    B = B[1:]

print(answer)