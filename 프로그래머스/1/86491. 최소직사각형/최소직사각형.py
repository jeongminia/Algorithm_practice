def solution(sizes):
    answer = []
    
    answer = []
        
    for wallet in sizes:
        check = wallet.copy()
        wallet[0] = min(check)
        wallet[1] = max(check)
    
    print(sizes)
    w = max([w[0] for w in sizes])
    h = max([h[1] for h in sizes])
    
    return w*h