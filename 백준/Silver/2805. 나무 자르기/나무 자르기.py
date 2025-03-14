import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 이분 탐색
start = 0
end = 1000000000  # 가능한 최대 높이

result = 0
while start <= end:
    mid = (start + end) // 2

    # 현재 높이(mid)로 잘랐을 때 얻을 수 있는 나무의 양 계산
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid

    # 목표량보다 더 많이 잘렸으면 높이를 높이기
    if total >= m:
        result = mid  # 현재 높이 저장
        start = mid + 1
    # 목표량보다 적게 잘렸으면 높이를 낮추기
    else:
        end = mid - 1

print(result)