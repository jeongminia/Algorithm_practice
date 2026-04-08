# 괄호가 열리면 쌓고 닫히면 지움
def solution(s):
    stack = []
    
    for char in s:
        if char == "(":
            stack.append(char)
        else:  
            if stack: 
                stack.pop()  
            else: 
                return False
    
    return len(stack) == 0