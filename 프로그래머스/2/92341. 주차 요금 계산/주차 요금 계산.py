def solution(fees, records):
    accumulate = dict()
    check = dict()

    for i in range(len(records)):
        records[i] = records[i].split()

    for i in range(len(records)):
        car_num = records[i][1]
        time = records[i][0]
        status = records[i][2]

        if status == 'IN':
            check[car_num] = time

        elif status == 'OUT':
            in_time = check.pop(car_num)
            in_h, in_m = map(int, in_time.split(":"))
            out_h, out_m = map(int, time.split(":"))
            duration = (out_h * 60 + out_m) - (in_h * 60 + in_m)
            accumulate[car_num] = accumulate.get(car_num, 0) + duration

    # 🧾 출차 안 된 차량 23:59 처리
    for car_num in check:
        in_time = check[car_num]
        in_h, in_m = map(int, in_time.split(":"))
        out_h, out_m = 23, 59
        duration = (out_h * 60 + out_m) - (in_h * 60 + in_m)
        accumulate[car_num] = accumulate.get(car_num, 0) + duration

    base_time, base_fee, unit_time, unit_fee = fees
    answer = []

    for car_num in sorted(accumulate.keys()):
        total_time = accumulate[car_num]
        if total_time <= base_time:
            fee = base_fee
        else:
            fee = base_fee + ((total_time - base_time + unit_time - 1) // unit_time) * unit_fee
        answer.append(fee)

    return answer
