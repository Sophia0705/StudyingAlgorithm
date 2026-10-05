def solution(my_string):
    answer = [0] * 52
    for c in my_string:
        if c.isupper():
            idx = ord(c) - 65
        else:   # 97 --> 26
            idx = ord(c) - 71
        answer[idx] += 1
    # print(ord('A'))
    # print(ord('a'))
    return answer