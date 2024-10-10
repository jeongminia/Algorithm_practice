from math import ceil

def solution(n, words):
    k = 0
    stack = [words[k]]
   # len_words = len(words)
    answer = [0, 0]
    
    while k != len(words)-1:
        k += 1
        new = words[k]
        
        if (new[0] == stack[-1][-1]) and (new not in stack) and (new not in stack):
            stack.append(new)
        else:
            stack.append(new)
            break
    
    if len(set(stack)) == len(words): 
        return answer
    else:
        k = len(stack)
        u = k/n
       # print(k/n)
        answer[1] = ceil(u)
        if k%n == 0:
	        answer[0] = n
        else:
            answer[0] = k%n
        
        return answer