from collections import deque

def cal_time_for_lst(time):
    s_h, s_m = map(int, time[0].split(':'))
    e_h, e_m = map(int, time[1].split(':'))
    return [s_h*60 + s_m, e_h*60 + e_m + 10]  # 퇴실 후 청소 10분 포함

def solution(book_time):
    book_time = sorted([cal_time_for_lst(bt) for bt in book_time])
    rooms = []

    for start, end in book_time:
        # 기존 방 중에서 재사용 가능한 방 찾기
        for i in range(len(rooms)):
            if rooms[i] <= start:
                rooms[i] = end
                break
        else:
            # 새 방이 필요함
            rooms.append(end)

    return len(rooms)
