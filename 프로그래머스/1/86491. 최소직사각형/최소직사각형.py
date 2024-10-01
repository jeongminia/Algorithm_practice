def solution(sizes):
        
    for wallet in sizes:
        check = wallet.copy()
        wallet[0] = min(check)
        wallet[1] = max(check)
    
    return max([w[0] for w in sizes]) * max([h[1] for h in sizes])