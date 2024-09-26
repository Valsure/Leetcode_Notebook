from typing import List


"""
暴力解法：取第一个字符串，遍历第一个字符串中的每个字符x
然后遍历列表中剩余字符串对应位置的字符是否是x
此方法时间复杂度为O(M*N)
空间复杂度O（1）

class Solution:
    def LongestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if strs:
            for i_index, i_value in enumerate(strs[0]):
                for j in strs[1:]:
                    if i_index >= len(j) or i_value != j[i_index] :
                        return prefix
                prefix += i_value
            return prefix
        else:
            return ""
            
"""

"""
解法2
取第一个字符串为prefix
依次遍历后面的字符串，将其与prefix比较，取最大公共前缀为prefix
遍历完最后一个字符串之后，prefix即为所求
此方法时间复杂度为O(M*N)?
M即为字符串列表的长度
"""
class Solution():
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if "" in strs:
            return ""
        prefix = strs[0]
        for item in strs[1:]:
            min_len = min(len(prefix), len(item))
            for i in range(min_len):
                if prefix[i] != item[i]:
                    prefix = prefix[:i]
                    break
                else:
                    prefix = prefix[:min_len]
        return prefix



if __name__ == '__main__':
    strs = ["flower","flow","flow","flaw"]
    print(Solution().longestCommonPrefix(strs))