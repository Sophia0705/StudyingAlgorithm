def solution(n, arr1, arr2):
    answer = []
    map1, map2 = [], []
    # 이진수 바꿔서
    for i in range(n):
        t1, t2 = bin(arr1[i])[2:], bin(arr2[i])[2:]
        if len(t1) < n:
            t1 = '0' * (n - len(t1)) + t1
        if len(t2) < n:
            t2 = '0' * (n - len(t2)) + t2
        map1.append(t1)
        map2.append(t2)
    
    # 벽 체크
    for i in range(n):
        temp = ''
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer