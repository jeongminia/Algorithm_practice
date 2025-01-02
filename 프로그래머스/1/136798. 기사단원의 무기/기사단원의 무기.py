def cal_num(num):
    cnt = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            cnt += 2  # i와 num // i는 서로 다른 약수
            if i * i == num:
                cnt -= 1  # 제곱수인 경우 중복된 약수 제거
        i += 1
    return cnt
        
def solution(number, limit, power):
    answer = 0
    lst = [cal_num(num) for num in range(1, number+1)]
	
    if limit >= max(lst):
        return sum(lst)
    else:
        for j in lst:
            if j <= limit:
                answer +=j
            else:
                answer += power
        return answer