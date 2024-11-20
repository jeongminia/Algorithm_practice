def solution(a, b):
    lst = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = [31, 29, 31, 30,
           31, 30, 31, 31,
           30, 31, 30, 31]
     
    answer = ''
    
    total_days = sum(day[:a-1]) + b - 1
    
    return lst[total_days % 7]