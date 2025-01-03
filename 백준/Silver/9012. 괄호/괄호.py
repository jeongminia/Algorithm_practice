import sys
input_data = sys.stdin.read().splitlines()
n = int(input_data[0])
string_lst = input_data[1:n+1]

for s in string_lst:
    temp_s = []
    i = 0
    is_valid = True

    while i != len(s):
        if s[i] == '(':
            temp_s.append(s[i])
        else:
            if len(temp_s) > 0:
                temp_s = temp_s[:-1]
            else:
                print('NO')
                is_valid = False
                break
        i += 1

    if is_valid and len(temp_s) == 0:
        print('YES')
    elif is_valid: 
        print('NO')