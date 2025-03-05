import sys
import heapq

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
lectures = [tuple(map(int, line.split())) for line in data[1:n+1]]
lectures.sort(key=lambda x: x[0])

heap = []  
heapq.heappush(heap, lectures[0][1])

for i in range(1, n):  
    start, end = lectures[i]

    if heap[0] <= start:
        heapq.heappop(heap) 

    heapq.heappush(heap, end)

print(len(heap)) 