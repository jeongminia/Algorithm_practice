# 입력 받기
n, m = map(int, input().split())
hear_set = set(input().strip() for _ in range(n))  # 듣도 못한 사람
see_set = set(input().strip() for _ in range(m))   # 보도 못한 사람

# 두 집합의 교집합을 구하고, 사전 순으로 정렬
result = sorted(hear_set & see_set)

# 결과 출력
print(len(result))
print("\n".join(result))