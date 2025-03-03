import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # N: 듣도 못한 사람 수, M: 보도 못한 사람 수
answer = []
not_listen = {input().strip() for _ in range(N)}
not_see = {input().strip() for _ in range(M)}

for listen in not_listen:
    if listen in not_see:
        answer.append(listen)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)