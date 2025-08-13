def solution(bandage, health, attacks):
    t, x, y = bandage[0], bandage[1], bandage[2]
    max_health = health
    last_time = attacks[-1][0]  
    timeline = [x]*(last_time+1)
        
    for att_time, hurt in attacks:
        timeline[att_time] -= (hurt+x)
    
    count = 0   # t되는지 체크
    idx = 0
    for sec in range(last_time+1):
        if timeline[sec] == x:  # 공격 없으면 회복
            count += 1
            health += x
            if count == t:  # 연속 회복
                health += y
                count = 0
        else: # 공격
            health += timeline[sec]
            count = 0
        # maxhealth 제한
        if health > max_health:
            health = max_health
        
        # 사망
        if health <= 0:
            return -1
        
    return health