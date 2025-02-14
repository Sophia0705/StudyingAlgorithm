import sys
input = sys.stdin.readline

N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]
answer = 1

# 정렬
start = sorted(time[0] for time in times)
end = sorted(time[1] for time in times)

room_cnt = 0
max_cnt = 0
s, e = 0, 0

while s < N:
    if start[s] < end[e]:   # 새로운 회의 시작
        room_cnt += 1
        max_cnt = max(max_cnt, room_cnt)
        s += 1
    else:   # 하던거 종료
        room_cnt -= 1
        e += 1

print(max_cnt)