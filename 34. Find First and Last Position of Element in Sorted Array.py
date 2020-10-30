class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n<1 or target < nums[0] or target > nums[-1]:
            return [-1,-1]
        else:
            pos = self.binary_search(nums, 0, len(nums), target)
            if pos == -1:
                return [-1,-1]
            else:
                low = pos
                high = pos
                while low >= 0 and nums[low] == target:
                    low -= 1
                while high < n and nums[high] == target:
                    high += 1

                return [low+1, high-1]


    def binary_search(self, nums, low, high, target):
        mid = (low + high) // 2
        if low < high:
            print(nums)
            if nums[mid] > target:
                return self.binary_search(nums,low, mid, target)
            elif nums[mid] < target:
                return self.binary_search(nums, mid+1, high, target)
            else:
                return mid
        else:
            return -1




if __name__ == '__main__':
    nums = [5,5, 7, 7, 8, 8, 10]
    sol = Solution()
    print (sol.searchRange(nums,5))
