def get_pos(n):
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    return keypad[n]

def solution(numbers, hand):
    answer = ''
    lnow, rnow = '*', '#'  # 시작 위치

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            lnow = num
        elif num in [3, 6, 9]:
            answer += 'R'
            rnow = num
        else:
            # 가운데 줄 -> 거리 계산
            ldist = abs(get_pos(lnow)[0] - get_pos(num)[0]) + abs(get_pos(lnow)[1] - get_pos(num)[1])
            rdist = abs(get_pos(rnow)[0] - get_pos(num)[0]) + abs(get_pos(rnow)[1] - get_pos(num)[1])

            if ldist < rdist:
                answer += 'L'
                lnow = num
            elif rdist < ldist:
                answer += 'R'
                rnow = num
            else:
                if hand == 'right':
                    answer += 'R'
                    rnow = num
                else:
                    answer += 'L'
                    lnow = num

    return answer
