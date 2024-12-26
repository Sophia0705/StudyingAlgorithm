# 30802 웰컴 키트
import sys
input = sys.stdin.readline

n = int(input())    # 참가자 수
wants = list(map(int, input().split()))  # 티셔츠 사이즈별 신청자 수
t, p = map(int, input().split())  # 티셔츠 단위 수 / 펜 묶음 수

minT = 0
for w in wants:
    temp = (w+t-1) // t
    minT += temp

print(minT)
print(n//p, n%p)