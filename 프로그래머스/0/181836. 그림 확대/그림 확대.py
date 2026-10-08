def solution(picture, k):
    answer = []
    for pic in picture:
        temp = ''
        for c in pic:
            temp += c * k
        for i in range(k):
            answer.append(temp)
    return answer