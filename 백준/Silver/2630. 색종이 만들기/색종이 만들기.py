import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])  
video = [list(map(int, row.split())) for row in data[1:N+1]] 

blue = 0
red = 0

def divide(x, y, size):
    global blue, red
    first_value = video[x][y]  

    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != first_value:  
                new_size = size // 2
                divide(x, y, new_size)  # 왼쪽 위
                divide(x, y + new_size, new_size)  # 오른쪽 위
                divide(x + new_size, y, new_size)  # 왼쪽 아래
                divide(x + new_size, y + new_size, new_size)  # 오른쪽 아래
                return  # 다르면 더 쪼개야 하므로 종료

    # 현재 영역이 모두 같은 색일 때
    if first_value == 0:
        blue += 1
    else:
        red += 1

divide(0, 0, N)
print(blue)
print(red)
