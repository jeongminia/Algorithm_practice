def solution(s):
    answer = []
    s = s[2:-2]           # 앞뒤 {{ }} 제거
    parts = s.split("},{")  # 각각의 집합 분리

    # 튜플의 길이가 작은 순서대로 정렬
    parts = sorted(parts, key=lambda x: len(x))
   # print(parts)
    for i in parts:
        for j in i.split(','):
            if (j not in [",", "'"]) and (int(j) not in answer):
   #             print(j)
                answer.append(int(j))
   #     print(i, "----")

    

    # 결과로 출력해야 하는 튜플의 원소 순서
    return answer
