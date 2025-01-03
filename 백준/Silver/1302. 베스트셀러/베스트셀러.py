import sys
from collections import Counter

input = sys.stdin.read
book_lst = [line for line in input().strip().split("\n") if line.strip()][1:]

book_dict = Counter(book_lst)
answer = []

for i in range(len(book_dict)):
    if list(book_dict.values())[i] == max(book_dict.values()):
        answer.append(list(book_dict.keys())[i])

print(sorted(answer)[0])