import sys
input = sys.stdin.readline

def upper(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r)//2
        if arr[mid] > target:
            r = mid
        else:
            l = mid+1
    return l


def lower(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r)//2
        if arr[mid] >= target:
            r = mid
        else:
            l = mid+1
    return l

n, m = map(int, input().split())    # n: 점 개수, m: 선분 개수
points = list(map(int, input().split()))    # 점의 좌표 - 점이 같은 좌표 가지지 X
points.sort()
for _ in range(m):
    x, y = map(int, input().split())
    print(upper(points, y) - lower(points, x))