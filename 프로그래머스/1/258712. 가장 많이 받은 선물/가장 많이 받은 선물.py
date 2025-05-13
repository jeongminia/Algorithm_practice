# 사람*사람 선물 기록표 [give, take]
def cal_record(friends, gifts):
    record = [[0]*len(friends) for _ in range(len(friends))]

    for i in range(len(gifts)):
        give, take = gifts[i].split(" ")
        giver, taker = friends.index(give), friends.index(take)
        record[giver][taker] += 1
    return record
        
# 사람 선물 기록표 [give, take, num]
def cal_present(friends, gifts):
    prepower = []
    cnt_present = [[0,0,0] for _ in range(len(friends))]
    
    for i in range(len(gifts)):
        giver, receiver = gifts[i].split(" ")

        id_giver, id_receiver = friends.index(giver), friends.index(receiver)
        cnt_present[id_giver][0] += 1
        cnt_present[id_receiver][1] += 1
    
    for person in cnt_present:
        person[2] = person[0] - person[1]
        prepower.append(person[2])
    
    return cnt_present, prepower
        
def solution(friends, gifts):
    this_month = [0]*len(friends)  # 이번 달에 선물 받는 개수

    record = cal_record(friends, gifts)
    cnt_present, prepower = cal_present(friends, gifts)
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:
                continue
            # i가 j에게 준 선물이 더 많은 경우
            if record[i][j] > record[j][i]:
                this_month[i] += 1
            # 주고받은 수 같고 선물 지수로 판별
            elif record[i][j] == record[j][i]:
                if prepower[i] > prepower[j]:
                    this_month[i] += 1

    return max(this_month)
