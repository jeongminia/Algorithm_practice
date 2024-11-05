def solution(cards1, cards2, goal):
    goal_lst = []
    
    for word in goal:
        
        if (len(cards1) > 0) and (word == cards1[0]) :
            k = cards1.pop(0)
            goal_lst.append(k)
                
        if (len(cards2) > 0) and (word == cards2[0]) :
            k = cards2.pop(0)
            goal_lst.append(k)
        
    if goal_lst == goal:
        return 'Yes'
    else:
        return 'No'