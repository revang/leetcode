#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

from typing import List

# @lc code=start


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        # @lc code=end
