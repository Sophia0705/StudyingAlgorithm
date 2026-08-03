# 범위 체크
def valid_check(x, y):
    if -5 <= x <= 5 and -5 <= y <= 5:
        return True
    return False

# 이동
def move(x, y, dir):
    if dir == 'U':
        y += 1
    elif dir == 'D':
        y -= 1
    elif dir == 'R':
        x += 1
    elif dir == 'L':
        x -= 1
    return x, y

def solution(dirs):
    answer = set()
    x, y = 0, 0
    
    for dir in dirs:
        nx, ny = move(x, y, dir)
        if not valid_check(nx, ny):
            continue
        # 좌표 아니고 경로 저장
        answer.add((x, y, nx, ny))
        answer.add((nx,ny, x, y)) # 경로 저장이니까 양방향
        
        x, y = nx, ny
    return len(answer) // 2