def solution(s, n):
    answer = ''
    for c in s:
        next = ''
        # print(ord('a'), ord('z'))   # 97, 122
        # print(ord('A'), ord('Z'))   # 65, 90
        if c == ' ':    # 빈칸은 건너뛰기
            answer += ' '
            continue
        if c.isupper():   # 대문자
            if ord(c) + n > 90:
                next = chr(ord(c)+n-26)
            else:
                next = chr(ord(c)+n)
        else:   # 소문자
            if ord(c) + n > 122:
                next = chr(ord(c)+n-26)
            else:
                next = chr(ord(c)+n)
        
        answer += next

    return answer