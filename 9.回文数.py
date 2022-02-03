#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        chars = list(str(x))
        begin, end = 0, len(chars)-1
        while begin < end:
            if chars[begin] != chars[end]:
                return False
            begin += 1
            end -= 1
        return True

# @lc code=end
