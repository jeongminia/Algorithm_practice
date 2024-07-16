from itertools import permutations

def solution(k, dungeons):
    cnt_lst = []
    for case in permutations(dungeons):
        stress = k
        cnt = 0

        for i in case:

            if stress >= i[0]:
                stress -= i[1]
                cnt += 1
            else:
                break
                
        cnt_lst.append(cnt)
    return max(cnt_lst)