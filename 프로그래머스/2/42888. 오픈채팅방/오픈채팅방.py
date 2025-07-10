def solution(record):
    answer = []
    who = {}
    for message in record:
        if "Enter" in message:
            who[message.split()[1]] = message.split()[2]
        elif "Change" in message:
            who[message.split()[1]] = message.split()[2]
    
    #print(who)
    for message in record:
        if "Enter" in message:
            answer.append(who[message.split()[1]]+"님이 들어왔습니다.")
        elif "Leave" in message:
            answer.append(who[message.split()[1]]+"님이 나갔습니다.")
    
    return answer