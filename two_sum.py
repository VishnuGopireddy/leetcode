#https://leetcode.com/problems/two-sum/
'''
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
'''


class Solution:
    def twoSum(self,nums,target):
        i = 0, j = len(nums)
        sum = nums[i] + nums[j]
        while i < j and sum != target:
            if sum < target:
                i = i + 1
            else:
                j = j - 1
        return indices


