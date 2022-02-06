#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#
from typing import List
# @lc code=start


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.row = len(self.matrix)
        self.column = len(self.matrix[0])
        self.matrix_sum = [[0]*(self.column+1) for _ in range(self.row+1)]
        for i in range(1, self.row+1):
            for j in range(1, self.column+1):
                self.matrix_sum[i][j] = self.matrix[i-1][j-1]+self.matrix_sum[i-1][j]+self.matrix_sum[i][j-1]-self.matrix_sum[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x1, y1, x2, y2 = row1+1, col1+1, row2+1, col2+1
        return self.matrix_sum[x2][y2]-self.matrix_sum[x1-1][y2]-self.matrix_sum[x2][y1-1]+self.matrix_sum[x1-1][y1-1]

# @lc code=end


def test():
    numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    assert numMatrix.sumRegion(2, 1, 4, 3) == 8
    assert numMatrix.sumRegion(1, 1, 2, 2) == 11
    assert numMatrix.sumRegion(1, 2, 2, 4) == 12
