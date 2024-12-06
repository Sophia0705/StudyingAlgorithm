def solution(bandage, health, attacks):
    max_health = health  # 최대 체력 저장
    current_health = health  # 현재 체력
    
    # attacks를 딕셔너리로 변환 (시간: 피해량)
    attack_dict = {time: damage for time, damage in attacks}
    
    # 마지막 공격 시간까지 순회
    last_attack_time = attacks[-1][0]
    consecutive_heal = 0  # 연속 성공 시간
    
    for time in range(1, last_attack_time + 1):
        # 공격이 있는 시간인 경우
        if time in attack_dict:
            current_health -= attack_dict[time]
            consecutive_heal = 0
            # 체력이 0 이하가 되면 -1 반환
            if current_health <= 0:
                return -1
        # 공격이 없는 시간인 경우
        else:
            # 기본 회복
            current_health += bandage[1]
            consecutive_heal += 1
            
            # 연속 성공 보너스
            if consecutive_heal == bandage[0]:
                current_health += bandage[2]
                consecutive_heal = 0
            
            # 최대 체력 초과하지 않도록 제한
            current_health = min(current_health, max_health)
    
    return current_health