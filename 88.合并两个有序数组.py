#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

"""
author : revang
date   : 2022-02-02
method : 双指针
"""

from typing import List

from numpy import sort

# @lc code=start


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         ans = []
#         idx1, idx2 = 0, 0
#         while idx1 < m or idx2 < n:
#             if idx1 == m:
#                 ans.append(nums2[idx2])
#                 idx2 += 1
#                 continue
#             if idx2 == n:
#                 ans.append(nums1[idx1])
#                 idx1 += 1
#                 continue
#             if nums1[idx1] <= nums2[idx2]:
#                 ans.append(nums1[idx1])
#                 idx1 += 1
#             else:
#                 ans.append(nums2[idx2])
#                 idx2 += 1
#         nums1[:] = ans  # 要理解为什么不是nums1=ans

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted = sorted+nums2[p2:]
                break
            if p2 == n:
                sorted = sorted+nums1[p1:]
                break
            if nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted
# @lc code=end
