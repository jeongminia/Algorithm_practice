def solution(phone_book):
   # answer = True
    phone_book.sort()
   # print(phone_book)
    
    for i in range(len(phone_book)):
        current = phone_book[i]
        
        if i < len(phone_book)-1:
            compare = phone_book[i+1]
            if compare.startswith(current) == True:
                return False
                break

    return True