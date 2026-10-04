def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        temp = myString[i:]
        if temp.startswith(pat):
            answer += 1
    return answer