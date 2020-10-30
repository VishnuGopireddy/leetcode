

def merge_sort(nums, low, high):
    if low< high:
        mid = (low + high) // 2
        merge_sort(nums,low,mid)
        merge(nums, low, mid, high)
        merge_sort(nums,mid+1,high)
        merge(nums, low, mid, high)
    else:
        return

def merge(nums,low,mid,high):
    left = [nums[i] for i in range(low, mid)]
    right = [nums[i] for i in range(mid,high)]
    temp1 = 0
    temp2 = 0
    i = low

    while temp1 < len(left) and temp2 < len(right):
        if left[temp1] <= right[temp2]:
            nums[i] = left[temp1]
            temp1 += 1
        else:
            nums[i] = right[temp2]
            temp2 += 1
        i += 1

    while temp1 < len(left):
        nums[i] = left[temp1]
        i += 1
        temp1 += 1

    while temp2 < len(right):
        nums[i] = right[temp2]
        i += 1
        temp2 += 1


nums = [10,44,0,1,5,3,7,2,8,4,77]
merge_sort(nums,0,len(nums))
print(nums)
# print(merge(nums,0,4,len(nums)))