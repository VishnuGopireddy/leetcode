#Given two binary strings, return their sum (also a binary string).

'''
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
'''


def addBinary(a,b):
    max_len = max(len(a),len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = []
    i = 1
    carry = 0
    s=0
    while(i <= max_len):
        s = int(a[-i]) + int(b[-i]) + carry

        if s == 1:
            carry = 0
        elif s == 2:
            carry = 1
            s = 0
        elif s==3:
            s = 1
            carry = 1
        result.append(str(s))
        i = i + 1
    if carry == 1:
        result.append(str(carry))

    result = result[::-1]
    print(''.join(result))

addBinary('1010','1011')

