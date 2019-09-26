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
        hash = {}
        for i in range(len(nums)):
            if i in hash:
                return [hash[i],i]
            else:
                diff = target - nums[i]
                hash.update({diff:i})
        return False

s = Solution()
nums = [2, 7, 11, 15]
target = 9

print(s.twoSum(nums,target))