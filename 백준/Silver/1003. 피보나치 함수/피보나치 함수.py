import sys
test_cases = int(sys.stdin.readline().rstrip())
inputs = [int(input()) for _ in range(test_cases)]

# 다이나믹 프로그래밍 적용: 호출된 값은 메모리에 저장하여 재호출을 방지
def fibonacci(n):
    # 피보나치 값을 저장할 리스트를 n+1 크기로 생성하고 0으로 초기화
    fibonacci_sequence = [0 for _ in range(n + 1)]
    fibonacci_sequence[0] = 0  # 피보나치 수열 초기값 설정
    
    if n == 0:
        return "1 0"  # n이 0일 경우, 0과 1의 호출 횟수를 반환
    elif n > 0:
        fibonacci_sequence[1] = 1  # 피보나치 수열 초기값 설정

    # 피보나치 수 계산
    for i in range(2, n + 1):        
        fibonacci_sequence[i] = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    
    # 0과 1이 호출된 횟수를 반환
    result = str(fibonacci_sequence[n - 1]) + " " + str(fibonacci_sequence[n])
    return result

for num in inputs:
    print(fibonacci(num))
