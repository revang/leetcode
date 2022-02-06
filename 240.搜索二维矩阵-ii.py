#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

from typing import List

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        column = len(matrix[0])
        i, j = 0, column-1
        while i < row and j >= 0:
            val = matrix[i][j]
            if val == target:
                return True
            elif val > target:
                j -= 1
            else:
                i += 1
        return False

# @lc code=end


def test():
    assert Solution().searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5) == True
    assert Solution().searchMatrix([], 0) == False
