def change_alpabet(k, n):
    dictionary = ['a', 'b', 'c', 'd', 'e',
                  'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p',
                  'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z'
                  ]*4
    return dictionary[dictionary.index(k)+n]


def solution(s, n):
    answer = ''
    temp = []

    for i in s:
        if i.isalpha():
            if i.isupper():
                i = i.lower()
                ii = change_alpabet(i, n).upper()
                temp.append(ii)
            else:
                temp.append(change_alpabet(i, n))
        else:
            temp.append(i)

   # print(temp)
    answer = ''.join(temp)
    return answer