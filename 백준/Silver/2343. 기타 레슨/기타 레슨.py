import sys
input = sys.stdin.readline

def counting(size):
    cnt = 1
    sumV = 0

    for lecture in lectures:
        if sumV + lecture > size:
            cnt += 1
            sumV = lecture
        else:
            sumV += lecture
    return cnt

def binary_search():
    ans = 0
    left, right = max(lectures), sum(lectures)
    while left <= right:
        mid = (left + right) // 2
        count = counting(mid)

        if count > m:
            left = mid+1
        else:
            ans = mid
            right = mid-1
    return ans

n, m = map(int, input().split())    # n: 강의 수, m: 블루레이 수
lectures = list(map(int, input().split()))
print(binary_search())
