def solution(phone_book):
    answer = True
    
    phone_book.sort()
  #  print(phone_book)
    
    # while 제거하고 for 문으로 하나씩 이동해주기
    current = phone_book[0]
    for j in phone_book[1:]:
        if current == j[:len(current)]:
            answer = False
            break
        current = j
        
    return answer