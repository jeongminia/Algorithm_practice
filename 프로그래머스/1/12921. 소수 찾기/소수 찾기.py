def solution(n):
    n_lst = [True] * (n + 1)  # n+1 크기의 배열을 True로 초기화
    n_lst[0] = n_lst[1] = False  # 0과 1은 소수가 아님
    
#    print(n_lst)
    
    # 2부터 n의 제곱근까지 검사
    for i in range(2, int(n**0.5) + 1):
 #       print(i)
        if n_lst[i]:
            # i의 배수를 False로 설정
            for j in range(i * i, n + 1, i):
                n_lst[j] = False
    
    # True인 인덱스만 소수이므로 그 개수를 셈
    return sum(n_lst)