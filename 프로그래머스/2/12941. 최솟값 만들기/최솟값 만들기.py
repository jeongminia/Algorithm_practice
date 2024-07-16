from collections import deque

def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse=True)
        
        
    return sum([i*j for i, j in zip(A, B)])