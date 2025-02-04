import sys

# 입력 받기
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
meetings = [tuple(map(int, line.split())) for line in data[1:N+1]]

# 종료 시간이 빠른 순서대로 정렬 (같은 종료 시간이면 시작 시간이 빠른 순서)
meetings.sort(key=lambda x: (x[1], x[0]))

end_time = 0
cnt = 0

for start, end in meetings:
    if start >= end_time:  
        end_time = end
        cnt += 1


print(cnt)
