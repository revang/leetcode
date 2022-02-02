#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

from typing import List

# @lc code=start


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            while nums[left] % 2 == 0 and left < right:
                left += 1
            while nums[right] % 2 != 0 and left < right:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return nums

# @lc code=end


def test():
    assert Solution().sortArrayByParity([3, 1, 2, 4]) == [4, 2, 1, 3]
