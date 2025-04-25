def solution(new_id):
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계 ; 일부 특수 문자 제거
    step_2 = ""
    for i in new_id:
        if i not in "~!@#$%^&*()=+[{]}:?,<>/":
            step_2+=i
            
    new_id = step_2  
    #print(new_id)
    
    # 3단계 ; 중복되는 . 제거
    step_3 = new_id[0]
    for i in new_id[1:]:
        if (step_3[-1] == '.') and (i == '.'):
            continue
        else:
            step_3+=i
    
    new_id = step_3
    #print(new_id)

    # 4단계 : 마침표(.)가 처음이나 끝에 위치한다면 제거
    if len(new_id) > 0 and (new_id[0] == '.'):
        new_id = new_id[1:]
    if len(new_id) > 0 and (new_id[-1] == '.'):
        new_id = new_id[:-1]

    #print(new_id)
            
    # 5단계 : new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if len(new_id) == 0:
        new_id = 'a'

    #print(new_id)

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    #print(new_id)

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    #print(new_id)
    
    
    return new_id