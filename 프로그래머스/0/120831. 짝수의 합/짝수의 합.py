def solution(n):
    if n%2 == 0:
        ans = [i for i in range(0, n+1,2)]
        answer = sum(ans)
    else:
        ans = [i for i in range(0, n,2)]
        answer = sum(ans)
    return answer