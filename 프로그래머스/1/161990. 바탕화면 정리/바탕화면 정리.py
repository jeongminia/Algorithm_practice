def solution(wallpaper):
    answer = []
    
    h, w = len(wallpaper), len(wallpaper[0])
    background = [[0]*w for i in range(h)]
    for i in range(h):
        item = wallpaper[i]
        for j in range(w):
            if item[j] == '#':
                background[i][j] = 1
                
    min_x, min_y, max_x, max_y = 51, 51, 0, 0
#    print(background)
    for i in range(h):
        item = background[i]
        for j in range(w): 
            if item[j] == 1:
                min_x = min(j, min_x)
                max_x = max(j+1, max_x)
                
                min_y = min(i, min_y)
                max_y = max(i+1, max_y)
    
    return [min_y, min_x, max_y, max_x]