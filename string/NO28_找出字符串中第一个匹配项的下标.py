"""
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。 
示例 1：
输入：
haystack = "sadbutsad", needle = "sad"
输出：
0
解释：
"sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
示例 2：
输入：
haystack = "leetcode", needle = "leeto"
输出：
-1
解释：
"leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
 提示：
• 1 <= haystack.length, needle.length <= 104
• haystack 和 needle 仅由小写英文字符组成

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            k = i
            for j in range(len(needle)):
                if(k>len(haystack)-1):
                    return -1
                if haystack[k] != needle[j]:
                    break
                k += 1

            if k-i == len(needle):
                return i
        return -1

class Solution1:
    def strStr(self, haystack, needle):
        
    


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("mississippi", "issipi"))