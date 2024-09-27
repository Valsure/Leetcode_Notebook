"""
class Solution:
    def judge1(self, s: str):
        return s == "{"

    def judge2(self, s: str):
        return s == "["

    def judge3(self, s: str):
        return s == "("

    def isValid(self, s: str) -> bool:
        judges = {
            "}": self.judge1,
            "]": self.judge2,
            ")": self.judge3,
        }  #通过字典实现类似switch的功能，目的是判断左右括号是否匹配

        if not s or len(s) % 2 or s[0] in judges:
            return False  #如果字符串为空/个数为奇数/第一个字符为右括号
        stack = []
        for item in s:
            if not stack and item in judges:
                return False  #如果栈为空且第一个字符为右括号
            if item in judges:
                if judges[item](stack[-1]):
                    stack.pop()
            #当出现右括号时，利用之前写的匹配规则，判断右括号的前一个是否为其对应的左括号
            #若是则弹出此右括号，若不是则直接返回Flase
                else:
                    return False
            else:
                stack.append(item)
        if not stack:
            return True#如果栈空了，说明所有括号都匹配并弹出
        else:
            return False
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # 初始化栈
        matching = {")": "(", "}": "{", "]": "["} # 创建对应关系字典
        for item in s:
            if item in matching.values():  # 如果是左括号
                stack.append(item)
            else:  # 如果是右括号
                if not stack or matching[item] != stack[-1]: # 检查是否匹配栈顶左括号
                    return False
                stack.pop()  # 匹配成功，出栈

        return not stack  # 如果栈为空，说明括号有效


if __name__ == '__main__':
    s = "([}}])"
    print(Solution().isValid(s))
