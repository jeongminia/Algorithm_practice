import sys

input = sys.stdin.read
people = input().splitlines()[1:]
dung = [(int(people[j].split(' ')[0]), int(people[j].split(' ')[1])) for j in range(len(people))]
ranks = []

for i in range(len(dung)):
    cnt = 0
    # print(dung[i])
    w, h = dung[i][0], dung[i][1]
    for j in range(len(dung)):
        if i != j: # 자기 자신 빼고
            if dung[j][0] > w and dung[j][1] > h:
               # print('yes')
                cnt += 1
       # print(cnt)
    ranks.append(cnt + 1)

print(" ".join(map(str,ranks)))