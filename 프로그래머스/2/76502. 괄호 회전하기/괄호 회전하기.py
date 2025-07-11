def check(s):
    st = []
    for chr in s:
        if chr in "([{":
            st.append(chr)
        else:
            if not st:
                return False
            if chr == ')' and st[-1] != '(':
                return False
            if chr == ']' and st[-1] != '[':
                return False
            if chr == '}' and st[-1] != '{':
                return False
            st.pop()
    return not st  # 스택이 비어 있어야 올바른 괄호

def solution(s):
    answer = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]  # i만큼 회전
        if check(rotated):
            answer += 1
    return answer