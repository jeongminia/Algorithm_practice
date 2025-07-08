def solution(babbling):
    cnt = 0
    
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace("aya", '1')
        babbling[i] = babbling[i].replace("ye", '2')
        babbling[i] = babbling[i].replace("woo", '3')
        babbling[i] = babbling[i].replace("ma", '4')
        
        if (babbling[i].isnumeric()) and ("11" not in babbling[i]) and ("22" not in babbling[i]) and ("33" not in babbling[i]) and ("44" not in babbling[i]):
            cnt+=1

    return cnt