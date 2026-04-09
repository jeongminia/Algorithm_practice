def solution(citations):
    # 1. 내림차순 정렬
    citations.sort(reverse=True)
    
    # 2. 순번(i+1)과 인용 횟수(cit) 비교
    for i, cit in enumerate(citations):
        # 인용 횟수가 현재 논문 편수(i+1)보다 작아지는 순간
        if cit < i + 1:
            return i
            
    # 모든 논문의 인용 횟수가 전체 논문 편수보다 크다면
    return len(citations)