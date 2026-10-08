def solution(a, b, c, d):
    answer = 0
    check = len(set([a, b, c, d]))
    if check == 1:
        answer = 1111 * a
    elif check == 2:
        if a == b == c and c != d:
            answer = (10 * a + d)**2
        elif a == c == d and d != b:
            answer = (10 * a + b)**2
        elif b == c == d and d != a:
            answer = (10 * b + a)**2
        elif a == b == d and d != c:
            answer = (10 * a + c)**2
        elif a == b and b != c and c == d:
            answer = (a + c) * abs(a - c)
        elif a == c and c != b and b == d:
            answer = (a + b) * abs(a - b)
        elif a == d and d != b and b == c:
            answer = (a + b) * abs(a - b)
    elif check == 3:
        if a == b and b!= c and c != d:
            answer = c * d
        elif a == c and c != b and b != d:
            answer = b * d
        elif a == d and d != b and b != c:
            answer = b * c
        elif b == c and c != a and a != d:
            answer = a * d
        elif b == d and d != a and a != c:
            answer = a * c
        elif c == d and d != a and a != b:
            answer = a * b
    elif check == 4:
        answer = min(a, b, c, d)
            
    return answer