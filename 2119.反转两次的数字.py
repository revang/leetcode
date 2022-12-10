#
# @lc app=leetcode.cn id=2119 lang=python3
#
# [2119] 反转两次的数字
#

# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num % 10 != 0 or num == 0

# @lc code=end


def test():
    assert Solution().isSameAfterReversals(526) == True
    assert Solution().isSameAfterReversals(1800) == False
    assert Solution().isSameAfterReversals(0) == True
