class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x < 0:
            reversed_s = "-" + s[1:][::-1]
        else:
            reversed_s = s[::-1]
        reversed_num = int(reversed_s)
        if reversed_num < -(2 ** 31) or reversed_num > (2 ** 31 - 1):
            return 0
        return reversed_num

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(-123))