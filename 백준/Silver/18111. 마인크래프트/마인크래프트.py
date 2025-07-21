# 18111. 마인크래프트
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split()) #B: 인벤토리
heights = [list(map(int, input().split())) for _ in range(N)]
minT, H = float('inf'), 0
flat = [h for row in heights for h in row]
# 목표 높이를 0부터 256까지 다 시도해보기
# 각 높이마다 필요한 시간 계산하기
# 현재 블록이 목표보다 높으면? → 제거 (2초)
# 현재 블록이 목표보다 낮으면? → 추가 (1초)
# 인벤토리 체크도 잊지 말기! (블록이 부족하면 그 높이는 불가능)
for h in range(min(flat), max(flat)+1):
    remove, add, time = 0, 0, 0
    for height in flat:
        if height > h:
            remove += height - h
            time += 2*(height - h)
        elif height < h:
            add += h - height
            time += h - height
    if B + remove >= add:
        if time < minT or (time == minT and h > H):
            minT = time
            H = h

print(minT, H)