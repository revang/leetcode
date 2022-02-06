#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

from typing import List
# @lc code=start

# 冒泡排序
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         size = len(nums)
#         for i in range(size-1):
#             for j in range(size-i-1):
#                 if nums[j] > nums[j+1]:
#                     nums[j], nums[j+1] = nums[j+1], nums[j]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quick(left, right):
            if left >= right:
                return nums
            pivot, i, j = left, left, right
            while i < j:
                while i < j and nums[j] > nums[pivot]:  # 要理解这两个同级的where顺序为什么不能换
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[j] = nums[j], nums[pivot]
            quick(left, j-1)
            quick(j+1, right)
            return nums
        quick(0, len(nums)-1)

# @lc code=end


def test():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(nums)
