# 15663. N과 M(9)

import sys
input = sys.stdin.readline

def DFS(depth):
    if len(temp) == M:
        print(*temp)
        return

    for i in range(N):
        if visited[i]:
            continue
        elif i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
            continue
        else:
            visited[i] = True
            temp.append(nums[i])

        DFS(depth+1)

        # 백트래킹
        temp.pop()
        visited[i] = False


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()  # 사전순 출력을 위해 정렬
temp, visited = [], [False] * N

DFS(0)
