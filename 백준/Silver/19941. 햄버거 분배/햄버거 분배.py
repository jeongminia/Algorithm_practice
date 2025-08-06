N, K = map(int, input().split()) # 식탁의 길이, 햄버거를 선택할 수 있는 길이
str_lst = input()

def solution(N, K, str_lst):
    table = list(str_lst)
    eaten = [False] * N  # 햄버거가 먹혔는지 여부
    answer = 0

    for i in range(N):
        if table[i] == 'P':
            # P는 왼쪽부터 K칸 안에 있는 H 중 아직 안 먹힌 것 우선 선택
            for j in range(max(0, i-K), min(N, i+K+1)):
                if table[j] == 'H' and not eaten[j]:
                    eaten[j] = True
                    answer += 1
                    break  # 이 사람은 햄버거 하나 먹었으니 종료

    return answer

print(solution(N, K, str_lst))
# print(solution(20, 1, "HHPHPPHHPPHPPPHPHPHP")) 