def solution(keymap, targets):
    answer = []
    key_dict = {}

    for k in keymap:
        for i in range(len(k)):
            if k[i] not in key_dict.keys():
                key_dict[k[i]] = i+1
            else:
                if key_dict[k[i]] > i:
                    key_dict[k[i]] = i+1
    
   # print(key_dict)

    for word in targets:
        cnt = 0
        for i in word:
            if i in key_dict.keys():
                cnt += key_dict[i]
            else:
                cnt = -1
                break
        answer.append(cnt)

    return answer