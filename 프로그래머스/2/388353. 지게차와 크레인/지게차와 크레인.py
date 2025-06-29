
#상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solution(storage, requests):
    N, M = len(storage), len(storage[0])
    answer = N*M
    status = [[0] * (M+2) for _ in range(N+2)]
    extracted = [[True] * (M+2) for _ in range(N+2)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            status[i][j] = storage[i-1][j-1]
            extracted[i][j] = False
    
    #크레인으로 인해서 뜬금없이 추출되어 바깥과 연결이 안 된 컨테이너를 다시 검사해서 바깥으로 처리하기
    def checkExternal():
        for y in range(1, N+1):
            for x in range(1, M+1):
                if status[y][x] != 0 and extracted[y][x]:
                    for dir in range(4):
                        ny, nx = y + dy[dir], x + dx[dir]
                        if status[ny][nx] == 0:
                            status[y][x] = 0
                            break
    
    #지게차로 빼기
    def forklift(req, target):
        nonlocal answer
        batch_list = []
        for y in range(1, N+1):
            for x in range(1, M+1):
                if target == status[y][x] and not extracted[y][x]:
                    #사방에서 적어도 한 면이 외부와 접촉되어 있어야 빼기 가능
                    for dir in range(4):
                        ny, nx = y + dy[dir], x + dx[dir]
                        if status[ny][nx] == 0:
                            batch_list.append((y, x))
                            break
        
        #[지게차] 배치로 한 번에 처리하기
        for y, x in batch_list:
            answer -= 1
            status[y][x] = 0 #이제는 외부로 처리
            extracted[y][x] = True
            checkExternal()
    
    #크레인으로 빼기
    def crain(req, target):
        nonlocal answer
        batch_list = []
        for y in range(1, N+1):
            for x in range(1, M+1):
                if target == status[y][x] and not extracted[y][x]:
                    batch_list.append((y, x))
        
        #[크레인] 배치로 한 번에 처리하기
        for y, x in batch_list:
            answer -= 1
            extracted[y][x] = True
            #사방에서 적어도 한 면이 외부와 접촉되어 있어야 외부로 처리 가능
            for dir in range(4):
                ny, nx = y + dy[dir], x + dx[dir]
                if status[ny][nx] == 0:
                    status[y][x] = 0
                    break
            checkExternal()
    
                            
    for req in requests:
        target = req[0]
        if len(req) == 1:
            forklift(req, target)
        else:
            crain(req, target)
        
        checkExternal()
        
    return answer