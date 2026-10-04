def solution(arr):
    answer = 0
    while True:
        temp = arr[:]  # 바꾸기 전 상태 복사 (체크용)
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1
        
        if temp == arr:
            return answer
        
        answer += 1