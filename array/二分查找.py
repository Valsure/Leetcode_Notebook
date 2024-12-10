from typing import List

def binary_search(nums:List[int], low, high, target):
    if low > high:
        return low
    mid = (low + high)//2
    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        high = mid-1
        return binary_search(nums, low, high, target)
    elif target > nums[mid]:
        low = mid+1
        return binary_search(nums, low, high, target)

print(binary_search([1,3,5,7], 0, 3, 4))