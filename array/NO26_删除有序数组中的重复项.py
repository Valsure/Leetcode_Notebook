from typing import Tuple, List
'''
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
判题标准:

系统会用下面的代码来测试你的题解:

int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有断言都通过，那么您的题解将被 通过。

'''

# class Solution:
#     def removeDuplicates(self, nums: list[int])
#         for i in range(len(nums) - 1, 0, -1):
#             if nums[i] == nums[i-1]:
#                 del nums[i]
#         return len(nums), nums


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                j += 1
                nums[j] = nums[i]

        return j+1


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9]
    solution = Solution()
    print(solution.removeDuplicates(nums))