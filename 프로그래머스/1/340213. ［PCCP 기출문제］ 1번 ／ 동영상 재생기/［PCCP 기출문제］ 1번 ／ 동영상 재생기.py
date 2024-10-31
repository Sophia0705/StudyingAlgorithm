def solution(video_len, pos, op_start, op_end, commands):
    # mm:ss를 초단위로 바꾸고
    def to_sec(t):
        time = int(t[:2]) * 60 + int(t[3:])
        return time
    
    # 다시 초단위를 mm:ss로 바꾸고
    def to_min(t):
        mm = int(t) // 60
        ss = int(t) % 60
        return f"{mm:02d}:{ss:02d}" 
    
    # 광고 스킵
    def skip(t):
        if op_start <= t <= op_end:
            return op_end
        return t
    
    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)
    
    # skip 함수로 초기 위치 체크
    pos = skip(pos)
    
    for command in commands:
        # 1. 먼저 이동
        if command == "prev":
            pos = max(0, pos-10)
        else:
            pos = min(video_len, pos+10)
        # 2. 그 다음에 광고 구간 체크
        pos = skip(pos)
        
    return to_min(pos)