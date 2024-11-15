from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], 2))