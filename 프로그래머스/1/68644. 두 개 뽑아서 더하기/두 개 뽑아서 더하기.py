from itertools import permutations
def solution(numbers):
    temp = set()
    perms = set(permutations(numbers, 2))
    for p in perms:
        temp.add(sum(p))
    listed_ans = sorted(list(temp))
    
    return listed_ans