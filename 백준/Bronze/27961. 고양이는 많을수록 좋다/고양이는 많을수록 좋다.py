n = int(input())
cats = 0
cnt = 0

while cats < n:
    if cats == 0:
        cats += 1
    elif cats * 2 <= n:
        cats *= 2
    else:
        cats = n

    cnt += 1

print(cnt)