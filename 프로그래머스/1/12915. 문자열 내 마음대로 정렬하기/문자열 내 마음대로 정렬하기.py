# 딕셔너리는 정렬할 때 items() 를 활용하여 정렬 -> sorted(dict_a.items())
# 사전 순으로 어떻게 정렬하면 좋은지 모르겠음

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x)) # 허무결과..