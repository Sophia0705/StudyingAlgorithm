def solution(s):
    answer = 0
    while s:
        x = s[0]
        cnt1, cnt2 = 1, 0   # 같은거, 다른거
        # 비교
        for i in range(1, len(s)):
            if s[i] == x:
                cnt1 += 1
            else:
                cnt2 += 1
            # 개수 비교
            if cnt1 == cnt2:
                answer += 1
                s = s[i+1:]
                break # for문 종료 -> 다시 while 쪽으로 가게
                
        else: 
            answer += 1 # 남은 문자열은 마지막 덩어리로 처리
            s = ''
    return answer