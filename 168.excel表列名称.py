#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         ans = ""
#         val = columnNumber
#         dic = [None, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#         while val > 0:
#             quotient, remainder = val//26, val % 26  # 商, 余数
#             ans = dic[remainder]+ans if remainder != 0 else ans
#             if quotient <= 26:
#                 ans = dic[quotient]+ans if quotient != 0 else ans
#                 break
#             val = quotient
#         return ans

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26+ord('A')))
            columnNumber = columnNumber//26
        ans.reverse()
        return "".join(ans)

# @lc code=end


def test():
    assert Solution().convertToTitle(1) == "A"
    assert Solution().convertToTitle(28) == "AB"
    assert Solution().convertToTitle(701) == "ZY"
    assert Solution().convertToTitle(2147483647) == "FXSHRXW"
    assert Solution().convertToTitle(26) == "Z"
