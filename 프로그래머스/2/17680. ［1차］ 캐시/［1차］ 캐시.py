def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [city.lower() for city in cities]

    while cities:
        city = cities.pop(0)
        if cacheSize:
            if not city in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                answer += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
        else:
            answer += 5
    return answer