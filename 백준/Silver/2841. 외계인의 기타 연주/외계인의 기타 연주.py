import sys

input = sys.stdin.read
data = input().splitlines()

N, P = map(int, data[0].split())
melody = [tuple(map(int, line.split())) for line in data[1:N+1]]

lines = [[] for _ in range(7)] 
cnt = 0  

for rownum, pnum in melody:
    # 기존에 눌러진 프렛이 있을 경우, 현재 프렛보다 높은 프렛들을 모두 pop
    while lines[rownum] and lines[rownum][-1] > pnum:
        lines[rownum].pop()
        cnt += 1  
        
    if not lines[rownum] or lines[rownum][-1] != pnum:
        lines[rownum].append(pnum)
        cnt += 1 

print(cnt)
