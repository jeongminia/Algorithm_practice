def solution(phone_book):
    answer = True
    phone_book2 = {}
    for i in phone_book:
        phone_book2[i] = len(i)
        
    # 딕셔너리 정렬
    phone_book = list(dict(sorted(phone_book2.items(), key=lambda x: x[1])).keys())
    phone_book.sort()
    
    # while 제거하고 for 문으로 하나씩 이동해주기
    current = phone_book[0]
    for j in phone_book[1:]:
        if current == j[:len(current)]:
            answer = False
            break
        current = j
        
    return answer