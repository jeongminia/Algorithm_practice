def solution(scores):
    wanho = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))  # 성과 높은 순, 태도 낮은 순
    
    max_attitude = 0
    answer_list = []

    for score in scores:
        if score[1] < max_attitude:
            # 성과는 높지만 태도가 낮음 → 이미 누군가에게 밀림 (탈락 대상)
            if score == wanho:
                return -1
        else:
            max_attitude = max(max_attitude, score[1])
            answer_list.append(score)

    # 살아남은 사람들 중 총합 계산
    total = [s[0] + s[1] for s in answer_list]
    wanho_total = wanho[0] + wanho[1]

    rank = sum(1 for t in total if t > wanho_total) + 1
    return rank
