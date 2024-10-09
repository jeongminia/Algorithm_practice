def solution(numbers, target):
    q = [0]
    
    for n in numbers:
      #  print('----------',n)
        s = []
        
        for _ in range(len(q)):
            x = q.pop()
       #     print(q)
            s.append(x + n)
            s.append(x + n*(-1))
       #     print(s)
        q = s.copy()
        
    return q.count(target)