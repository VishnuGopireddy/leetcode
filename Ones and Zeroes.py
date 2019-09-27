#https://leetcode.com/problems/ones-and-zeroes/

'''
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.


Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

'''

def findMaxForm(strs, m, n):
    count = 0
    for i in strs:
        if check_str(i,m,n):
            count = count + 1
    return count
def check_str(s,m,n):
    if s.count('0') <= m and s.count('1')<= n:
        return True
    else:
        return False

Array = {"10", "0001", "111001", "1", "0"}
m = 5
n = 3
print(findMaxForm(Array,m,n))