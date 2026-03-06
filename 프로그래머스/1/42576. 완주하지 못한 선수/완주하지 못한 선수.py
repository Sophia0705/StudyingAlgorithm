from collections import Counter

def solution(participant, completion):
    part_dict = Counter(participant)
    for com in completion:
        if com in part_dict.keys():
            part_dict[com] -= 1

    ans = [key for key, count in part_dict.items() if count > 0]
    answer = str(ans[0])
    return answer