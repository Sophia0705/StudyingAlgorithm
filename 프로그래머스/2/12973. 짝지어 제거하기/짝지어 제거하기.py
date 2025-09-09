def solution(s):
    answer = 0
    strs = list(s.rstrip())
    st = []
    
    for i in range(len(strs)):
        if st and strs[i] == st[-1]:
            st.pop(-1)
        else:
            st.append(strs[i])
    if len(st) == 0:
        answer = 1
    return answer