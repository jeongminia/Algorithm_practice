from collections import deque

def convert_to_minutes(time):
    h, m = int(time[:2]), int(time[3:])
    return h * 60 + m

def convert_to_time_str(minutes):
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"

def solution(n, t, m, timetable):
    crew_times = deque(sorted([convert_to_minutes(time) for time in timetable]))
    
    # 셔틀 도착 시간 계산
    shuttle_times = [convert_to_minutes("09:00") + t * i for i in range(n)]
    
    for idx, shuttle in enumerate(shuttle_times):
        # 각 셔틀에 최대 m명까지 태운다
        passengers = []
        while crew_times and crew_times[0] <= shuttle and len(passengers) < m:
            passengers.append(crew_times.popleft())

        # 마지막 셔틀이면 콘의 도착 시각 결정
        if idx == n - 1:
            if len(passengers) < m:
                # 자리 남았으면 셔틀 도착 시각에 와도 됨
                return convert_to_time_str(shuttle)
            else:
                # 자리 없으면 마지막으로 탄 크루보다 1분 일찍 도착해야 함
                return convert_to_time_str(passengers[-1] - 1)
