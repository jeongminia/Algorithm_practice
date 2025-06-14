'''
isdigit 함수를 사용하여 해당 문자가 숫자인지 문자인지 판단하기
'''

def solution(s):
    answer = ""
    table = {'zero':0, 'one':1, 'two':2, 'three':3,
            'four':4, 'five':5, 'six':6, 'seven':7,
            'eight':8, 'nine':9}
    
    if s.isdigit() == True:
        return int(s)
    
    else:
        temp = "" # 영단어로 변환하기 전
        for i in range(len(s)):
            print(temp)
            if s[i].isdigit() == False:
                temp+=s[i]
                if temp in table:
                    answer+=str(table[temp])
                    temp = ""
            else:
                answer+=s[i]
            #print(answer, temp)
            
        return int(answer)
    
    