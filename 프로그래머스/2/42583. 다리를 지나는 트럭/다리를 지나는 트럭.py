def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridge_weight = 0
    
    while bridge:
        answer += 1  # 시간 경과
        bridge_weight -= bridge.pop(0)  # 다리 하나씩 지나감
        
        if truck_weights:
            # 현재 다리의 무게 합과 새로운 트럭 무게 더함
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)  # 트럭 진입 불가

        # 트럭이 다 지나갔으면 종료
        if not bridge and not truck_weights:
            break
    
    return answer