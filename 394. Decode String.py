
s = 'a0[kl]'

s = '2[abc]3[cd]ef'
s = "3[a2[c]]"
# s = 'abcd'

i = 0
n = len(s)
decode = ''

while i < n:
    if not s[i].isdigit():
        decode += s[i]
        i += 1

    else:
        num = ''
        while s[i] != '[':
            num += s[i]
            i += 1
        replicate_str = ''
        if s[i] == '[':
            i += 1
        while s[i] != ']':
            replicate_str += s[i]
            i += 1
        if s[i] == ']':
            i += 1

        decode += replicate_str * int(num)

print(decode)

