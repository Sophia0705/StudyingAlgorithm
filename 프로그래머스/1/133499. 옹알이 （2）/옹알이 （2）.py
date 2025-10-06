def solution(babbling):
    answer = 0
    pronounces = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        temp = b
        # 발음을 숫자로 치환
        for i, p in enumerate(pronounces):
            temp = temp.replace(p, str(i))
        chk = True
        for idx in range(4):
            if str(idx) * 2 in temp:
                chk = False
                break
        if not chk:
            continue
        
        # 잔여 체크
        remain = False
        for c in temp:
            if c not in '0123':
                remain = True
        
        if not remain:
            answer += 1
    return answer