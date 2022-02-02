#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

from typing import List

# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                continue
            left += 1
        return right+1

# @lc code=end


def test():
    assert Solution().removeElement([3, 2, 2, 3], 3) == 2
    assert Solution().removeElement([], 1) == 0
    assert Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert Solution().removeElement([1], 1) == 0
