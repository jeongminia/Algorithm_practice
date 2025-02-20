import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])  
video = [list(map(int, list(row))) for row in data[1:N+1]]  # 2차원 리스트로 변환


def divide(x, y, size):
    first_value = video[x][y]  

    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != first_value:  
                print("(", end="") 

                new_size = size // 2
                divide(x, y, new_size)  # 왼쪽 위
                divide(x, y + new_size, new_size)  # 오른쪽 위
                divide(x + new_size, y, new_size)  # 왼쪽 아래
                divide(x + new_size, y + new_size, new_size)  # 오른쪽 아래

                print(")", end="")  
                return

    # 현재 영역이 모두 같은 숫자라면, 해당 숫자만 출력
    print(first_value, end="")


# 쿼드트리 압축 실행
divide(0, 0, N)
