def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] == arr[i]:
                stk.pop(-1)
                i += 1
            else:
                stk.append(arr[i])
                i += 1
    
    if not stk:
        stk = [-1]
    
    return stk