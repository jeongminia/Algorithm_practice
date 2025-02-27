def solution(routes):
    routes.sort(key = lambda x : x[1])
    #print(routes)

    answer = 1

    previous_t = routes[0][1]
    for car in routes[1:]:
        if previous_t < car[0]:
            answer += 1
            previous_t = car[1]
    
    return answer