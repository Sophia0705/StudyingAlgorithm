def solution(arr):
    r, c = len(arr), len(arr[0])
    dif = abs(r - c)
    
    if r > c:
        for i in range(r):
            arr[i].extend([0] * dif)
    
    elif r < c:
        temp = [[0] * c for i in range(dif)]
        arr.extend(temp)
    
    return arr