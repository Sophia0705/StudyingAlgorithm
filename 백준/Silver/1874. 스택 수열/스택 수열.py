import sys

n = int(input())
target = [int(input()) for _ in range(n)]  # 목표 수열

stack = []        # 스택
result = []       # 연산 기록 (+, -)
current = 1       # 현재 넣을 수
possible = True   # 수열 생성 가능 여부

for num in target:
    # 스택에 필요한 숫자까지 다 넣기
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    
    # 스택의 맨 위 숫자가 목표 숫자와 일치하는지 확인
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        # 일치하지 않으면 수열을 만들 수 없음
        possible = False
        break

if possible:
    for op in result:
        print(op)
else:
    print("NO")