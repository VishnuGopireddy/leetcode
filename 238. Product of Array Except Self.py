import math
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [0] * n
        right = [0] * n
        i = 0
        while i < n:
            if i == 0:
                left[i] = 1
            else:
                left[i] = (left[i-1] * nums[i-1])
            i += 1
        i = n-1
        while i >=0:
            if i == n-1:
                right[i] = 1
            else:
                right[i] = right[i+1] * nums[i+1]
            i -= 1
        sol = []
        for i in range(n):
            sol.append(left[i] * right[i])
        print(left)
        print(right)
        print(sol)
        return sol

sol = Solution()
# nums = [4,5,1,8,2]
nums = [0,0]
print(sol.productExceptSelf(nums))