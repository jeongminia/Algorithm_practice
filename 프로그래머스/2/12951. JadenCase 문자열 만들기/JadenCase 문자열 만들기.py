def solution(s):
    answer = ''
    
    for i in range(len(s)):
       # 
        if s[i-1] == " ":
            answer+=s[i].upper()
        elif answer == "" and s[i].isdigit() == False:
             answer+=s[i].upper()
        elif answer != "" and s[i].isdigit() == False:
            answer+=s[i].lower()
        elif s[i].isdigit():
            answer+=s[i]
            
    
    return answer