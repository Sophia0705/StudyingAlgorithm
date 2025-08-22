# 9996. 한국이 그리울 땐 서버에 접속하지
import sys
input = sys.stdin.readline

N = int(input())
pt1, pt2 = input().rstrip().split('*')
n1, n2 = len(pt1), len(pt2)
for _ in range(N):
    file = input().rstrip()
    # pt1과 pt2 길이가 체크할 파일보다 크면 검사X
    if n1 + n2 > len(file):
        print('NE')
        continue

    # pt1 체크
    if file[:n1] == pt1:
        check1 = True
    else:
        check1 = False

    # pt2 체크
    parsed = file[len(file)-n2:]
    if len(file) >= n2:
        if parsed == pt2:
            check2 = True
        else:
            check2 = False
    else:
        check2 = False

    if check1 and check2:
        print('DA')
    else:
        print('NE')