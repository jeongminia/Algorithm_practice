def solution(genres, plays):
    dic1 = {} # 곡 정보
    dic2 = {} # 장르 총 점수
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
 #   print(dic1)
 #   print(dic2)
    
    answer = []
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True): # 속한 노래가 많이 재생된 장르 먼저 수록
     #   print(k, v)
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]: # 장르 내에서 많이 재생된 노래 / 고유번호가 낮은 노래 / 최대 두 곡
            answer.append(i)

    return answer