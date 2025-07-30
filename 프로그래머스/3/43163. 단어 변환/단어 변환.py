from collections import deque

def is_convertible(a, b): 
    return sum(x != y for x, y in zip(a, b)) == 1 # 다른 글자 수가 하나여야만 연결될 수 있음

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append((begin, 0))  
    visited = set()

    while queue:
        current, count = queue.popleft()
        if current == target:
            return count

        for word in words:
            if word not in visited and is_convertible(current, word):
                visited.add(word)
                queue.append((word, count + 1))

    return 0
