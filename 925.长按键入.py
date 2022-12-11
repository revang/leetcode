#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left, right = 0, 0
        while right < len(typed):
            if left < len(name) and name[left] == typed[right]:
                left += 1
                right += 1
            elif right > 0 and typed[right-1] == typed[right]:
                right += 1
            else:
                return False

        return left == len(name)

# @lc code=end


def test():
    assert Solution().isLongPressedName(name="alex", typed="aaleex") == True
    assert Solution().isLongPressedName(name="saeed", typed="ssaaedd") == False
    assert Solution().isLongPressedName(name="leelee", typed="lleeelee") == True
    assert Solution().isLongPressedName(name="alexd", typed="ale") == False
