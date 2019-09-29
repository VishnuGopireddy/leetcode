#https://leetcode.com/problems/ugly-number/
'''
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:
Input: 6
Output: true
Explanation: 6 = 2 × 3

'''


def ugly(num):
    ugly = 0
    if num < 1:
        return False
    while num > 1 and ugly == 0:
        if num % 2 == 0:
            num = num // 2
        elif num % 3 == 0:
            num = num // 3
        elif num % 5 == 0:
            num = num // 5
        else:
            ugly = 1
    if ugly == 0:
        return True
    else:
        return False


num = 14
print(ugly(num))