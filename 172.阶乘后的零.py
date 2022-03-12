#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else int(n/5)+self.trailingZeroes(int(n/5))

# @lc code=end


def test():
    assert Solution().trailingZeroes(3) == 0
    assert Solution().trailingZeroes(5) == 1
    assert Solution().trailingZeroes(12) == 2
