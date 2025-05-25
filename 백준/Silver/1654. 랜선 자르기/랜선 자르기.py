import sys

input = sys.stdin.readline
K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

# 모든 랜선을 길이 mid로 잘랐을 때 몇 개가 나오는지 계산
def can_cut(length):
    count = 0
    for cable in cables:
        count += cable // length
    return count >= N # 만약 개수 >= N이면? → 길이를 더 늘릴 수 있는지 확인 → low = mid + 1

def binary_search(low, high):
    while low <= high: # 입력받은 랜선 길이 중 최댓값을 high로 설정 (이 이상은 어차피 못 자름)
        mid = (low + high) // 2
        if can_cut(mid):  
            low = mid + 1
        else:
            high = mid - 1
    return high

print(binary_search(1, max(cables)))