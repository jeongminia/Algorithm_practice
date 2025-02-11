import sys
from itertools import combinations

input = sys.stdin.read
data = input().splitlines()

L, C = map(int, data[0].split()) 
letters = sorted(data[1].split())

mo = ['a', 'e', 'i', 'o', 'u']
ja = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", 
      "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"  ]

for i in combinations(letters, L):
    if (len(list(set((i)) & set(mo))) >= 1) and (len(list(set(i) & set(ja))) > 1):
        print(''.join(i))
