while True:
    chrs = input()
    if chrs == '.':
        break
    stack = []
    check = 'yes'
    for chr in chrs:
        if chr in '([': # 여는 괄호 스택에 담기
            stack.append(chr)
        elif chr == ')':
            if not stack or stack [-1] != '(':
                check = 'no'
                break
            stack.pop()
        elif chr == ']':
            if not stack or stack [-1] != '[':
                check = 'no'
                break
            stack.pop()

    if stack:
        check = 'no'

    print(check)