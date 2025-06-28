def check(s):
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}') or (top == '[' and ch != ']'):
                return False
    return not stack

def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        rotated = s[i:] + s[:i]
        if check(rotated):
            answer += 1
    return answer
