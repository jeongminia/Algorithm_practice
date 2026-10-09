def solution(strings, n):
    answer = []
    
    
    print(strings)
    strings.sort(key=lambda x: (x[n], x), reverse=False)
    return strings