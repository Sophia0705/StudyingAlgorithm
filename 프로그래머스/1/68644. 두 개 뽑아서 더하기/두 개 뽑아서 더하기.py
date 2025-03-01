def solution(numbers):
    temp = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            temp.append(numbers[i] + numbers[j])
    answer = sorted(set(temp))
    return answer