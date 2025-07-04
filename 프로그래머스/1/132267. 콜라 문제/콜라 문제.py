def solution(a, b, n):
    answer = 0

    while n:
        gift = (n//a)*b
        answer += gift
        rest = n%a # 나머지

       # print(gift, rest, n)
        # 상빈이가 있는 콜라병
        n = gift+rest
        
        
        if gift == 0:
            break


    return answer