import sys

input = sys.stdin.read
data = input().splitlines()

T = int(data[0]) 
index = 1 

test_cases = []

for _ in range(T):
    N = int(data[index])  
    applicants = [tuple(map(int, data[i].split())) for i in range(index + 1, index + 1 + N)]
    
    test_cases.append(applicants)
    index += N + 1 


def solution(applicants):
    applicants.sort(key=lambda x: x[0])  # 서류 성적 기준 정렬

    best_speech = float('inf')  # 면접 성적의 최적 기준
    count = 0  

    for doc, speech in applicants:
        if speech < best_speech:  # 면접 순위가 더 좋은 경우
            count += 1
            best_speech = speech  # 면접 순위 갱신

    return count


for applicants in test_cases:
    print(solution(applicants))
