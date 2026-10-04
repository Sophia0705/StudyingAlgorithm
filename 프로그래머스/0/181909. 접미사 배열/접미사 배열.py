def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        ch = my_string[i:]
        answer.append(ch)
    answer.sort()
    return answer