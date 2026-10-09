from collections import Counter

def solution(s):
    answer = 0
    s_cnt = Counter(s)
    # print(s_cnt)
    if len(s_cnt)%2==1:
        return 0
    else:
        if s_cnt["{"]==s_cnt["}"]:
            pass
        else:
            return 0
        if s_cnt["("]==s_cnt[")"]:
            pass
        else:
            return 0
        if s_cnt["["]==s_cnt["]"]:
            pass
        else:
            return 0
    
    s = [j for j in s]
    for x in range(len(s)):
        print(x)
        stack = []
        
        for i in s:
            if stack==[]:
                stack.append(i)
            else:
                if stack[-1]=="[" and i=="]":
                    stack.pop(-1)
                elif stack[-1]=="{" and i=="}":
                    stack.pop(-1)
                elif stack[-1]=="(" and i==")":
                    stack.pop(-1)
                else:                # 짝이 안 맞으면 쌓기
                    stack.append(i)
        if stack==[]:
            answer+=1
        
        move = s.pop(0)
        s.append(move)
        
        
    
    return answer