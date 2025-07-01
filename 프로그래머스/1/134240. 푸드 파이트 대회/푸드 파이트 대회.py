from collections import deque
def solution(food):
    answer = deque(['0'])
    len_food = len(food)

    for i in range(len_food-1,0,-1):
        what = food[i]//2
        times = i
        #print(what, times)
        if what!=0:
            while what:
                answer.appendleft(str(times))
                answer.append(str(times))
                what-=1

    return "".join(answer)