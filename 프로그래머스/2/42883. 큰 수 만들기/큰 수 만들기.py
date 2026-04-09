def solution(number, k):
    stack = []
    
    for num in number:
        # 스택에 값이 있고, 지울 기회가 남았고, 현재 숫자가 스택 끝보다 크면 제거
        while (stack) and (k > 0) and (stack[-1]<num):
            stack.pop()
            k -= 1
        
        # 2. 현재 숫자를 스택에 쌓음
        stack.append(num)
      #  print(stack)
    
    # 리스트가 내림차순으로 정렬되어 있어서 불가피하게 아무것도 지우지 못한 케이스를 대비하여 그냥 슬라이스
    if k > 0:
        stack = stack[:-k]
        
    return "".join(stack)