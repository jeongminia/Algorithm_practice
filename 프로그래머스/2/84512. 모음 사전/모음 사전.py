from itertools import product

def solution(word):
    lst = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    for i in range(1, 6):
        for p in product(lst, repeat=i):
            dictionary.append("".join(p))
    
    dictionary.sort()
    
    return dictionary.index(word) + 1