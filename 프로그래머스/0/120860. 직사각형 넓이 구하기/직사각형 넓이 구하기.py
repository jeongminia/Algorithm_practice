def solution(dots):
    
    height = []
    widht = []
    
    
    for pos in dots:
        widht.append(pos[0])
        height.append(pos[1])
    
    w_len = abs(max(widht)-min(widht))
    h_len = abs(max(height)-min(height))
    
    return w_len*h_len