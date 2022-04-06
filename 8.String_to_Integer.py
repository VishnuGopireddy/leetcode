s = 'a +123'

def solution(s):
    num = ''
    has_seen_char = True
    for i, j in enumerate(s):
        if ord(j) == 45 or ord(j) == 43:
            if 49 <= ord(s[i+1]) <=57:
                has_seen_char = False
                num += j
        elif 49 <= ord(j) <= 57:
            has_seen_char = False
            num += j
        elif ord(j) != 33 and has_seen_char != False:
            has_seen_char = True
        print(has_seen_char)

    if has_seen_char:
        return 0
    num = int(num)
    print(num)
    if -(2**31) > num:
        return -(2**31)
    if (2**31)-1 < num:
        return (2**31)
    return num

print(solution(s))