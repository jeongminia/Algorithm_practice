from itertools import permutations

def solution(expression):
    answer = 0
    lst = []
    role = []
    
    temp = ""
    for i in range(len(expression)):
        if expression[i] in "-*+":
            lst.append(temp)
            lst.append(expression[i])
            role.append(expression[i]) 
            temp = ""
        else:
            temp += expression[i]
    lst.append(temp)  # 마지막 숫자 누락 방지

    role = list(set(role))
    
    for cas in permutations(role, len(role)):
        test = lst[:]
        for op in cas:
            stack = []
            i = 0
            while i < len(test):
                if test[i] == op:
                    a = int(stack.pop())
                    b = int(test[i+1])
                    if op == '+':
                        stack.append(str(a + b))
                    elif op == '-':
                        stack.append(str(a - b))
                    elif op == '*':
                        stack.append(str(a * b))
                    i += 2  # skip operator and right operand
                else:
                    stack.append(test[i])
                    i += 1
            test = stack  # 다음 연산자로 넘어갈 때 갱신

        answer = max(answer, abs(int(test[0])))  # 절댓값으로 비교

    return answer
