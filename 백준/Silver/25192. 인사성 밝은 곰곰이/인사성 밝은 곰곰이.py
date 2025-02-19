import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])  
chat_logs = data[1:N+1]

cnt = 0
user_set = set() 

for k in chat_logs:
    if k == "ENTER":
        user_set.clear()  
    elif k not in user_set:
        user_set.add(k)
        cnt += 1  

print(cnt)
