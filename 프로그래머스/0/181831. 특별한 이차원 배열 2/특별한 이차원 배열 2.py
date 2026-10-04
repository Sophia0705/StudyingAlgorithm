def solution(arr):
    check = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == arr[j][i]:
                check += 1
    if check == n * n:
        return 1
    return 0