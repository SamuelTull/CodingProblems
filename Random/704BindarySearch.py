def searchInsert(nums, target):
    left = -0.5
    right = len(nums) - 0.5
    while left != right:
        mid = int((left + right) / 2)
        if target < nums[mid]:
            right = mid - 0.5
        elif target > nums[mid]:
            left = mid + 0.5
        else:
            return mid
    return int(left + 0.5)


def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    while left != right:
        mid = (left + right) // 2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left if target <= nums[left] else left + 1


searchInsert([1, 3], 0)
searchInsert([1, 3, 5, 6], 5)
