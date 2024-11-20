def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]
   # k = 0
    
    for k in range(len(answer)):
        for j in range(len(arr1[0])):
            answer[k][j] = arr1[k][j] + arr2[k][j]
        
   #     k += 1
    
    return answer