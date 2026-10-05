def solution(my_string, queries):
    ans = my_string[:]
    for query in queries:
        s, e = query[0], query[1]
        cut = ans[s:e+1]
        revs = cut[::-1]
        left, right = ans[:s], ans[e+1:]
        ans = left + revs + right

    return ans