def solution(number, k):
    stack = []
    
    for num in number:
        while (k > 0) and (stack) and (stack[-1] < num):
    #        print(stack)
            stack.pop() # 작은 숫자 제거
            k -= 1
        stack.append(num)
    
  #  print(k)
   
    # 이미 정렬이 다 되어 있어서 소거를 못시켰다면 .. 
    # 내림차순으로 정렬되어 있어서 작은 숫자를 제거할 기회
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)
