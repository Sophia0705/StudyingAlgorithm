def timetosec(s):
    h, m, s = map(int, s.split(':'))
    sec = h*60*60 + m*60 + s
    return sec

def sectotime(sec):
    h, m, s = str(sec//3600), str((sec%3600)//60), str(sec%60)
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    if len(s) == 1:
        s = '0' + s
    time = f'{h}:{m}:{s}'
    return time

def solution(play_time, adv_time, logs):
    sec_play = timetosec(play_time)
    sec_adv = timetosec(adv_time)
    timeline = [0] * (sec_play +2)  # 시청 변화량 기록
    for log in logs:
        temp = log.split('-')
        s, e = timetosec(temp[0]), timetosec(temp[1])
        timeline[s] += 1
        timeline[e] -= 1
    
    # 매초 시청자 수 계산
    for i in range(1, sec_play+1):
        timeline[i] += timeline[i-1]
    
    # 0~i초까지 총 시청 시간 계산
    for i in range(1, sec_play+1):
        timeline[i] += timeline[i-1]
    
    # 광고 구간 합 비교
    max_time = timeline[sec_adv-1]
    ans = 0
    
    for start in range(sec_play-sec_adv+1):
        end = start + sec_adv -1
        total = timeline[end] - timeline[start-1]
        if total > max_time:
            max_time = total
            ans = start

    return sectotime(ans)