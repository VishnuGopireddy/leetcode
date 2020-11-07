'''
Ex: Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
'''

'''
This problem can be solved in 3 ways.
1. Brute force O(N*3)
2. DP O(N*2)
3. Manacher Algorithm O(N*2)
'''
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        ans = ""
        dp = [[0] * n for _ in range(n)]
        for gap in range(n):
            i = 0
            for j in range(gap, n):
                if s[i] == s[j]:
                    if gap <= 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j]:
                        ans = max(ans, s[i:j + 1], key=len)
                i += 1
        for i in dp:
            print(i)
        print(ans)
if __name__ == '__main__':
    sol = Solution()
    sol.longestPalindrome('aaabbaa')


