# 항상  [1, 2, 3, 1]

def solution(ingredient):
    answer = 0
    
  #  print(ingredient.pop(0)) # 맨 앞 뽑아내기
  #  print(ingredient.pop(-1)) # 맨 뒤 뽑아내기
    
    check=""
    for i in ingredient:
        check+=str(i)
    
    if "1231" not in check:
        return 0
    else:
        stack=[]
        for i in ingredient:
            if len(stack)>=3:
                if stack[-1]==3 and stack[-2]==2 and stack[-3]==1 and i==1:
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.pop(-1)
                    answer+=1
                else:
                    stack.append(i)
            else:
                stack.append(i)
          #  print(stack)
                
    
    
    return answer