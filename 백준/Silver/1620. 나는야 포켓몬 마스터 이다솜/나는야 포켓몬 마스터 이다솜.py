import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # N: 포켓몬 개수, M: 문제 개수
# N개만큼 포켓몬 dict (번호->이름, 이름->번호)
num2name = {}
name2num = {}

# 딕셔너리 저장
for i in range(1, N+1):
    name = input().strip()
    num2name[i] = name
    name2num[name] = i

# input 중 마지막 M개만큼은 문제
# 그럼 이 문제를 dict에서 빼서 답해야 함
for _ in range(M):
    todo = input().strip()
    if todo.isdigit():
        print(num2name[int(todo)])
    else:
        print(name2num[todo])
