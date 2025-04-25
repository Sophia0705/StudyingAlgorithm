def solution(N, stages):
    answer = []
    temp = []

    # 각 스테이지에 도달한 사람 수를 구하기
    p = len(stages)  # 총 사용자 수
    
    # 각 스테이지별 실패율 계산
    for stg in range(1, N + 1):  # 1번부터 N번까지 스테이지
        # 해당 스테이지에 도달한 사람들 (stg 이상인 사람들)
        reached = sum(1 for stage in stages if stage >= stg)
        
        # 해당 스테이지에서 실패한 사람들 (stg인 사람들)
        failed = stages.count(stg)
        
        if reached == 0:  # 해당 스테이지에 도달한 사람이 없으면 실패율 0으로 처리
            fail_rate = 0
        else:
            fail_rate = failed / reached
        
        # 실패율과 스테이지 번호를 튜플로 저장
        temp.append((stg, fail_rate))
    
    # 실패율을 기준으로 내림차순 정렬
    temp.sort(key=lambda x: x[1], reverse=True)
    
    # 실패율이 높은 순으로 스테이지 번호만 답안에 저장
    answer = [x[0] for x in temp]

    return answer
