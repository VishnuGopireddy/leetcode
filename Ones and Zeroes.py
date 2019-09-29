class Solution:
    def findMaxForm(self, strs, m, n):
        count = 0
        for i in strs:
            if self.check_str(i, m, n):
                count = count + 1
        return count

    def check_str(self,s, m, n):
        if s.count('0') <= m and s.count('1') <= n:
            return True
        else:
            return False
sol = Solution()
lst = ["10","0","1"]
print(sol.findMaxForm(lst,1,1))