#https://leetcode.com/problems/reverse-integer/
'''
Example:
Input: -123
Output: -321
'''
class Solution:
    def reverse(self, x):
        num = x
        if num >= 0:
            num = str(num)[::-1]
            num =  int(num)
        else:
            num = str(num)[1:]
            num = -int(num[::-1])
            num =  num
        if -2**31 <= num <= (2**31)-1:
            return num
        else:
            return 0

s = Solution()
print(s.reverse(-121))