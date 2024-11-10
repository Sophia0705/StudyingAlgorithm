# 4153 직각삼각형
while True:
    a, b, c = map(int, input().split())
    temp = [a, b, c]
    temp.sort()
    c = temp[-1]
    a = temp[0]
    b = temp[1]
    if a == 0 and b == 0 and c == 0:
        break

    if c**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')

