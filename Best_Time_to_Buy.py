#121. Best Time to Buy and Sell Stock

def best_time_stock(nums):
    n = len(nums)
    low, high = 0, 0

    profit = 0
    for i in range(1,n):
        if nums[i] < nums[low]:
            low = i

        if nums[i] > nums[high]:
            high = i

        if high < low:
            high = low

        if profit < nums[high] - nums[low]:
            profit = nums[high] - nums[low]

    return profit

nums = [7,1,5,3,6,4]
print(best_time_stock(nums))