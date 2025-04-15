import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    data = input().strip()

    if " " in data:
        command, num = data.split()
        num = int(num)

        if command == 'add':
            S.add(num)

        elif command == 'remove':
            S.discard(num)  # remove 대신 discard 쓰면 안전

        elif command == 'check':
            print(1 if num in S else 0)

        elif command == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.add(num)
    else:
        if data == 'all':
            S = set(range(1, 21))
        elif data == 'empty':
            S = set()
