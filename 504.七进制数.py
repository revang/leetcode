#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        if num == 0:
            return "0"
        elif num > 0:
            while num:
                a, b = num//7, num % 7
                ans = str(b)+ans
                num = a
            return ans
        else:
            num = -num
            while num:
                a, b = num//7, num % 7
                ans = str(b)+ans
                num = a
            ans = "-"+ans
            return ans


# @lc code=end

def test():
    assert Solution().convertToBase7(100) == "202"
    assert Solution().convertToBase7(-7) == "-10"
