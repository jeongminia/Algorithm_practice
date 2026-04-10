def solution(people, limit):
    answer = 0
    people.sort()
    
    start = 0
    end = len(people) - 1
    
    while start <= end:
        # 가장 무거운 사람과 가장 가벼운 사람을 같이 태워본다
        if people[start] + people[end] <= limit:
            start += 1  # 가벼운 사람도 같이 탔으므로 다음 사람으로 이동
        
        end -= 1
        answer += 1
        
    return answer