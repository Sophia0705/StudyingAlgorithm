def solution(numbers, hand):
    # 키패드
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    # 현재 위치
    left = keypad['*']
    right = keypad['#']
    
    def dist(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    ans = ''
    for num in numbers:
        if num in [1, 4, 7]:
            ans += 'L'
            left = keypad[num]
        elif num in [3, 6, 9]:
            ans += 'R'
            right = keypad[num]
        else:
            # 거리 계산해서 판별
            target = keypad[num]
            l_dist = dist(left, target)
            r_dist = dist(right, target)
            
            if l_dist < r_dist:
                ans += 'L'
                left = target
            elif r_dist < l_dist:
                ans += 'R'
                right = target
            else:   # 거리 같을 때 --> 손잡이!
                if hand == 'left':
                    ans += 'L'
                    left = target
                else:
                    ans += 'R'
                    right = target
                    
    return ans