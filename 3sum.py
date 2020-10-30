def threeSum(nums):
    n = len(nums)
    if n < 3:
        return []
    nums.sort()
    i, j, k = n, -1, -1
    sol = []

    for k in range(n - 2):
        j = k + 1
        i = n - 1
        if k > 0 and nums[k] == nums[k-1]:
            continue
        else:
            while j < i:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    i -= 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    sol.append([nums[k], nums[j], nums[i]])
                    j += 1
                    i -= 1
                    while j < n and nums[j] == nums[j-1]:
                        j += 1
                    while i > 0 and nums[i] == nums[i+1]:
                        i -= 1

    print(sol)
    # import itertools
    # sol.sort()
    # return list(k for k, _ in itertools.groupby(sol))

nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
threeSum(nums)