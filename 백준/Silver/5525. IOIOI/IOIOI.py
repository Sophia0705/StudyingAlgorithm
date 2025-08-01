n = int(input())
m = int(input())
s = input()

count = 0
i = 0

while i < m - 1:
    # "IO"로 시작하는 부분을 찾음
    if s[i:i+2] == "IO":
        pattern_count = 0
        # 연속된 "IOI" 패턴의 개수를 셈
        while i < m - 2 and s[i:i+3] == "IOI":
            pattern_count += 1
            i += 2  # "IOI"에서 다음 "IOI"로 이동 (2칸씩)
        
        # P_N 패턴이 몇 개 들어있는지 계산
        if pattern_count >= n:
            count += pattern_count - n + 1
    
    i += 1

print(count)