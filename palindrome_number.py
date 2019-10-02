#https://leetcode.com/problems/palindrome-number/
'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true
'''
class Solution:
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
s = Solution()
print(s.isPalindrome(-121))