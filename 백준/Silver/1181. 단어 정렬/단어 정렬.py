import sys
input = sys.stdin.read
data = input().splitlines()

words = list(set(data[1:]))
words.sort(key = lambda x : (len(x), x))

for i in words:
    print(i)