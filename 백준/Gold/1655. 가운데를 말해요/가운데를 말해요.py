import sys
import heapq

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
num_lst = list(map(int, data[1:]))

minh = [] 
maxh = [] 

for i in range(N):
    num = num_lst[i]

    # 최대 힙에 하나 더 들어가게
    if len(maxh) == len(minh):
        heapq.heappush(maxh, -num) 
    else:
        heapq.heappush(minh, num)

    # 최대힙의 루트값이 최소힙의 루트값 보다 작아야하기에 '값 교환' 진행
    if minh and -maxh[0] > minh[0]:
        left = -heapq.heappop(maxh)
        right = heapq.heappop(minh)
        heapq.heappush(maxh, -right)
        heapq.heappush(minh, left)

    print(-maxh[0])