def solution(s):
    s = list(s)
 #   print(s)
    stack = []
    k = 0
    
    while k != len(s):        
        #print('s >>>> ', s)
        
        new = s[k]
      #  print(new)
        
        if len(stack) > 0:
            if (new == stack[-1]):
                stack.pop()
            else:
                stack.append(new)
        elif len(stack) == 0:
            stack.append(new)
            
      #  print(stack)
    
        k += 1
        
    if len(stack) == 0:
        return 1
    else:
        return 0