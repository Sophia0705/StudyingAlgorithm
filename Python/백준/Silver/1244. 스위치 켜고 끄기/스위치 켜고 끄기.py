
def toggle(idx):
    if lst[idx] == 0:
        lst[idx] = 1
    else:
        lst[idx] = 0

def do1(idx):
    k = 1
    while k*idx <= switch_n:
        toggle(k*idx)
        k += 1
    return lst

def do2(i):
    toggle(i)
    k = 1
    while i-k >= 0 and i+k <= switch_n:
        if lst[i-k] == lst[i+k]:
            toggle(i-k)
            toggle(i+k)
            k += 1
        else: break
    return lst

switch_n = int(input())    # 스위치 개수
lst = [-1] + list(map(int, input().split()))   # 스위치 상태
n = int(input())    # 학생수
stu_lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    sex = stu_lst[i][0]
    no = stu_lst[i][1]
    if sex == 1:
        do1(no)
    elif sex == 2:
        do2(no)

lst.pop(0)

for num in range(0, switch_n, 20):
    print(*lst[num:num+20])

