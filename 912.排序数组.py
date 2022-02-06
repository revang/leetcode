#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

from typing import List

# @lc code=start


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick(left, right):
            if left >= right:
                return nums
            pivot, i, j = left, left, right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[j] = nums[j], nums[pivot]
            quick(left, j-1)
            quick(j+1, right)
            return nums
        return quick(0, len(nums)-1)
        # @lc code=end
