def solution(left, right):
    answer = 0
    nums = [i for i in range(left, right+1)]
    for n in nums:
        cnt = 0
        for i in range(1, n+1):
            if n % i == 0:
                cnt += 1
        
        if cnt % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer