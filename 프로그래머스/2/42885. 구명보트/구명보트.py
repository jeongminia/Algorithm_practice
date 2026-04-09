def solution(people, limit):
    people.sort() 
    
    start = 0                 
    end = len(people) - 1     
    boat = 0
    
    while start <= end:
        # 가장 무거운 사람과 가장 가벼운 사람을 같이 태울 수 있는지 확인
        if people[start] + people[end] <= limit:
            # 같이 탈 수 있으면 가벼운 사람도 출발(인덱스 증가)
            start += 1
            
        # 무거운 사람은 무조건 보트에 탐
        end -= 1
        
        # 보트 한 대 추가
        boat += 1
            
    return boat