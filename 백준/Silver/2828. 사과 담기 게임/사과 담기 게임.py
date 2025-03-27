N, M = map(int, input().split())      
J = int(input())                       
apples = [int(input()) for _ in range(J)] 

left = 1
right = M
routes = 0

for apple in apples:
    if apple < left:
        routes += (left - apple)
        left = apple
        right = left + M - 1
    elif apple > right:
        routes += (apple - right)
        right = apple
        left = right - M + 1
        
print(routes)