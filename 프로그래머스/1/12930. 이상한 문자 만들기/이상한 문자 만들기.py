def solution(s):
    s_lst = s.split(' ')
    answer = []
    
    
    for i in s_lst:
    #    print(i)
        k = ''
        for j in range(len(i)):
         #   print(j)
            if j%2 == 0:
                u = i[j].upper()
            else:
                u = i[j].lower()
            k += u
        answer.append(k)
    
    return ' '.join(answer)