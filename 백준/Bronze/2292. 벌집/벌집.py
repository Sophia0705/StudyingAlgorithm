n = int(input())
cnt = 1     # 지나는 방의 개수
limit = 1   # 현재 테두리 최댓값
chk = 1     # 6의 배수 체크용

while n > limit:
    limit += 6 * chk
    chk += 1
    cnt += 1

print(cnt)