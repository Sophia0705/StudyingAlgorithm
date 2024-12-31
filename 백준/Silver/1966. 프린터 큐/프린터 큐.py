from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())    # n: 문서 개수, m: 몇 번째
    priorities = deque(map(int, input().split()))
    targets = deque(range(n))    # 각 문서 원래 인덱스 저장
    cnt = 0

    while True:
        if priorities[0] == max(priorities):    # 현재 문서가 가장 높은 우선순위
            cnt += 1
            if targets[0] == m: # 찾는 문서일 때
                print(cnt)
                break
            priorities.popleft()    # 인쇄
            targets.popleft()

        else:   # 더 높은 우선순위 있으면
            priorities.append(priorities.popleft()) # 뒤로 보내기
            targets.append(targets.popleft())