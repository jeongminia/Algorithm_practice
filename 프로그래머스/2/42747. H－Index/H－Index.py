def solution(citations):
    citations = sorted(citations, reverse=True)
    
    for i, citation in enumerate(citations):
        if citation <= i + 1:
            return i  # 순번을 반환
    
    return len(citations)  # 모든 논문이 순번 이상으로 인용된 경우

        