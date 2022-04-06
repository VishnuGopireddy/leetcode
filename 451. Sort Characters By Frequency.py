"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.


Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict = {i: 0 for i in s}
        for i in s:
            my_dict[i] += 1
        my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        return "".join([i * j for i, j in my_dict])


if __name__ == '__main__':
    sol = Solution()
    s = "aabdbdbd"
    sort_str = sol.frequencySort(s)
    print(sort_str)



