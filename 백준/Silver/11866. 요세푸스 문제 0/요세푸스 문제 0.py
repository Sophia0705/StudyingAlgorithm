import sys
input = sys.stdin.readline
from collections import deque

def solve(n, k):
    Q = deque(range(1, n + 1))  # 1~n까지의 사람들
    result = []

    while Q:
        # k-1번 앞에서 빼서 뒤로 넣기
        for _ in range(k - 1):
            Q.append(Q.popleft())

        # k번째 사람 제거하고 결과에 추가
        result.append(Q.popleft())

    return result


n, k = map(int, input().split())
answers = solve(n, k)
print('<' + ', '.join(map(str, answers)) + '>')