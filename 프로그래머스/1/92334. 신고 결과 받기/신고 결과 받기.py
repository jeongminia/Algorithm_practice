from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)  # 중복 제거

    reported_by = defaultdict(set)  # 유저별 신고자 기록
    user_idx = {user: i for i, user in enumerate(id_list)}  # 유저 인덱스 기록

    #print(report, reported_by, user_idx)

    for r in report:
        a, b = r.split()
        reported_by[b].add(a)
    
    #print(reported_by)

    for b, reporters in reported_by.items():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[user_idx[reporter]] += 1

    return answer