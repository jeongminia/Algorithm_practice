import sys

input = sys.stdin.read

k = sorted(input(), reverse=True)

print("".join(k))