def solution(arr1, arr2):
    # 행렬의 행,열의 수
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    
    answer = [[0]*c2 for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            # 2개 행렬 데이터 곱해서 answer 리스트에 추가
            for k in range(c1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            
    return answer