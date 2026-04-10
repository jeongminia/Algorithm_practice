from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for case in permutations(dungeons):
   #     print(case)
        
        stress=k
        md = 0
        for j in case:
            ms, ds = j[0], j[1]
            if stress>=ms:
                stress-=ds
                md+=1
                answer=max(md,answer)
            else:
                break

    return answer