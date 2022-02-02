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
        pos, m, n = m+n-1, m-1, n-1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[pos] = nums1[m]
                pos, m = pos-1, m-1
            else:
                nums1[pos] = nums2[n]
                pos, n = pos-1, n-1
        while n >= 0:
            nums1[pos] = nums2[n]
            pos, n = pos-1, n-1
# @lc code=end
