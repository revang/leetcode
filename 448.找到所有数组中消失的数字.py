#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

from typing import List
# @lc code=start


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s1 = set(range(1, len(nums)+1))
        s2 = set(nums)
        return list(s1-s2)

# @lc code=end


def test():
    assert Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert Solution().findDisappearedNumbers([1, 1]) == [2]
