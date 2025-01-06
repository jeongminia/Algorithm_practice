from collections import Counter

def solution(weights):
    answer = 0
    weight_cnt = Counter(weights)

    for weight, count in weight_cnt.items():
        if count > 1:
            answer += count * (count - 1) // 2

    unique_weights = sorted(weight_cnt.keys())
    # print(unique_weights)
    
    for i in range(len(unique_weights)):
        for j in range(i + 1, len(unique_weights)):
            a, b = unique_weights[i], unique_weights[j]
            
            if (b == a * 2) or (b == a * 3 / 2 and (a * 3) % 2 == 0) or (b == a * 4 / 3 and (a * 4) % 3 == 0):
                answer += weight_cnt[a] * weight_cnt[b]

    return answer