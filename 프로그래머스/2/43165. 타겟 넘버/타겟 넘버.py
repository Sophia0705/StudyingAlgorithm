def dfs(numbers, target, idx, values):
    global cnt

    # 노드 끝까지 갔고, target과 같으면 (답 찾았을 때)
    if idx == len(numbers):
        if values == target:
            cnt += 1
        return  # 끝에 도달은 했지만 target과 다를 때(else 필요 없음)

    # 재귀함수 호출
    dfs(numbers, target, idx+1, values+numbers[idx])    # 더할 때
    dfs(numbers, target, idx+1, values-numbers[idx])   # 뺄 때



# dfs 함수 호출하는 solution 함수
def solution(numbers, target):
    global cnt
    cnt = 0
    dfs(numbers, target, 0, 0)
    return cnt