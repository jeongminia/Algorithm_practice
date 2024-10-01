def solution(people, limit):
    answer = len(people)
    people.sort()  
    i = 0  
    j = len(people) - 1  
      
    while i < j:  
        if people[i] + people[j] <= limit: 
            answer -= 1  
            i += 1  # 가벼운 사람을 다음 사람으로 이동
        j -= 1  # 무거운 사람은 항상 보트에 태움
    
    return answer 
