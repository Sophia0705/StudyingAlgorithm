def solution(arr):
    twolist = [2**i for i in range(0, 11)]
    for i in range(1000):
        l = len(arr)
        if l in twolist:
            return arr
        arr.append(0)