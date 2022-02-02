#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

from typing import List

# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        low, high = 0, len(nums)-1
        while low < high:
            pivot = low+(high-low)//2
            if nums[pivot] < nums[high]:  # 后半部分有序, 最小值在前半部分
                high = pivot
            elif nums[pivot] > nums[high]:  # 前半部分有序, 最小值在后半部分
                low = pivot+1
            else:
                high -= 1
        return nums[low]

        # @lc code=end


def test():
    assert Solution().findMin([1, 3, 5]) == 1
    assert Solution().findMin([2, 2, 2, 0, 1]) == 0
