'''
board: 게임 화면의 격자의 상태가 담긴 2차원 배열
moves: 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열

'''

def solution(board, moves):
    answer = 0
    n = len(board)
    
    temp = []
    for now in moves:
        now = now-1
        
        for i in range(n):
            if board[i][now] != 0:
                temp.append(board[i][now])
                board[i][now] = 0
                break
        
        if len(temp) > 1:
            if temp[-1] == temp[-2]:
                temp.pop()
                temp.pop()
                answer += 2
     #   print(temp)
            
    
    
    return answer