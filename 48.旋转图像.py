#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

from typing import List
# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        matrix_new = [[0]*size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                matrix_new[j][size-i-1] = matrix[i][j]
        matrix[:] = matrix_new
        print(matrix)

# @lc code=end


def test():
    Solution().rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
