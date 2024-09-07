# 16637 괄호 추가하기
import sys
input = sys.stdin.readline
N = int(input())     # 수식의 길이
expression = list(input().strip())  # 수식
maxV = -2**31

# 계산기
def cal(x, op, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y

# dfs로 완전탐색 & 재귀
def dfs(idx, value):
    global maxV

    # 다 수행했으면
    if idx >= N - 1:
        maxV = max(maxV, value)
        return

    # 괄호 안 쓴 경우
    if idx + 2 < N:     # 현재 위치에서 숫자, 연산자, 숫자가 모두 존재하는 경우
        next_value = cal(value, expression[idx+1], int(expression[idx+2]))
        dfs(idx+2, next_value)  # 다음 위치로 이동하여 재귀 호출 

    # 괄호 쓴 경우
    if idx + 4 < N:     # 현재 위치에서 괄호 안의 계산을 수행할 수 있는 경우
        # 괄호 안의 계산 수행
        temp_value = cal(int(expression[idx+2]), expression[idx+3], int(expression[idx+4]))
        # 괄호 결과를 이용하여 전체 계산 수행
        next_value = cal(value, expression[idx+1], temp_value)  
        dfs(idx+4, next_value)   # 다음 위치로 이동하여 재귀 호출

dfs(0, int(expression[0]))
print(maxV)