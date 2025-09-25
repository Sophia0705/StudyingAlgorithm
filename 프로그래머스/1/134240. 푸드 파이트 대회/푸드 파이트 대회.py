# 왼쪽-> 오른쪽 / 중앙: 물 (먼저 먹으면 승리) / 오른쪽 -> 왼쪽
# 각 음식이 //2 되는 만큼만 해야 양쪽 다 나눠먹을 수 있다
def solution(food):
    part = ''
    for i in range(1, len(food)):
        part += str(i) * (food[i]//2)
    reversed_part = part[::-1]
    answer = part + '0' + reversed_part
    return answer

