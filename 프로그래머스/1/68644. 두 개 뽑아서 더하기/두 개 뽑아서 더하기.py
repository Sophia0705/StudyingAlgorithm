def solution(numbers):
    answer = set()
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            temp = numbers[i] + numbers[j]
            if temp not in answer:
                answer.add(temp)
    ans = list(answer)
    ans.sort()

    return ans