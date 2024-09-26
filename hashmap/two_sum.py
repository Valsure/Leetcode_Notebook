from typing import List


"""
#双重循环的方式，时间复杂度为O(n2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

"""
#哈希表的方式，时间复杂度为O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,8,11,15], 23))