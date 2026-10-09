def solution(s):
    answer = -1
    stack = []
    
    for i in s:
        if stack==[]:
            stack.append(i)
        else: # 빈 스택이 아니라면
            if i == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(i)
     #   print(stack)
    
    
    if stack==[]:
        return 1
    else:
        return 0