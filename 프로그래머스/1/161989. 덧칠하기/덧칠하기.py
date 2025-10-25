def solution(n, m, section):
    answer = 0
    arr = [0] * (n+1)
    # 칠할 구역에 -1
    for sec in section:
        arr[sec] = -1
    
    for i in range(1, n+1):
        if arr[i] == -1:
            answer += 1
            # 롤러칠
            for j in range(i, min(i+m, n+1)):
                arr[j] = 0

    return answer