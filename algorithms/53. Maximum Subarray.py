#two solutions for this.
#1. Kadane's' Algorithm (DP)
#Divide and Conqur
nums = [-2,1,-3,4,-1,2,1,-5,4]

def sol(nums):
    n = len(nums)
    if n<2:
        return nums

    res = [nums[0]] * n
    maax = nums[0]

    for i in range(1,n):
        if (res[i-1] + nums[i]) > nums[i]:
            res[i] = nums[i] + res[i-1]
        else:
            res[i] = nums[i]

        if res[i] > maax:
            maax = res[i]

    print(res, maax)

nums = [1,2]
sol(nums)