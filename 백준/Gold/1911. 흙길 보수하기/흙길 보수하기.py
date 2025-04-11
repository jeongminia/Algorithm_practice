N, L = map(int, input().split())
puddles = [list(map(int, input().split())) for _ in range(N)]
puddles.sort()

plank = puddles[0][0]
paper = 0

for start, end in puddles:
    if plank > end:
        continue

    elif plank < start:
        plank = start

    dist = end - plank
    remainder = 1
    
    if dist % L == 0:
        remainder = 0

    cnt = dist // L + remainder
    plank += cnt * L
    paper += cnt

print(paper)  