def solution(s):
    answer = True
    stack=[]
    for x in s:
        if stack==[] and x==")":
            return False
        elif x=="(":
            stack.append(x)
        elif stack!=[] and x==")":
            stack.pop(-1)
            
    if stack==[]:
        return True
    else:
         return False