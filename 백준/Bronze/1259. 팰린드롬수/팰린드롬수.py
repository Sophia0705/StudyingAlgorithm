while True:
    pel = input()
    if pel == '0':
        break
    if pel == pel[::-1]:
        print('yes')
    else:
        print('no')