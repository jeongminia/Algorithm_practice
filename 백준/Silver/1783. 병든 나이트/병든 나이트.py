# 가능한 한 많은 칸을 방문
N, M = map(int, input().split())

if N == 1:
    print(1)
    exit()
elif N == 2:
    print(min(4, (M + 1) // 2))
    exit()
elif (N >= 3) and (M < 7): # 모든 이동 방식 사용 못함
    print(min(4, M))
    exit()
else:
    print(M-2)