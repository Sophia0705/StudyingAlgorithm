def solution(s):
    answer = ''
    numdict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    temp = ''
    for c in s:
        if c.isdigit():
            answer += c
            continue
        else:
            temp += c
        if temp in numdict.keys():
            t = numdict[temp]
            answer += t
            temp = ''
    return int(answer)