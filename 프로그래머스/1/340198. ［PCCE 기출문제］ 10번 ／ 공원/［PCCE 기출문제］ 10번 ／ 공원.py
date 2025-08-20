def solution(mats, park):   # mats: 돗자리 한변 길이, park: 공원 자리배치도
    N = len(park)
    M = len(park[0])
    mats.sort(reverse=True)
    for mat in mats:
        for i in range(N - mat+1):
            for j in range(M - mat+1):
                check = True
                for r in range(mat):
                    for c in range(mat):
                        if park[i+r][j+c] != '-1':
                            check = False
                    if not check:
                        break
                if check:
                    return mat
    return -1