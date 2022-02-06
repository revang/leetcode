#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

from typing import List

# @lc code=start


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        res = 0
        size_row, size_column = len(matrix), len(matrix[0])
        dp = [[0]*size_column for _ in range(size_row)]
        for i in range(size_row):
            for j in range(size_column):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == "1":
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                res = max(res, dp[i][j]*dp[i][j])
        return res

# @lc code=end


def test():
    assert Solution().maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]]) == 4

    assert Solution().maximalSquare([["0", "1"], ["1", "0"]]) == 1

    assert Solution().maximalSquare([["0"]]) == 0

    assert Solution().maximalSquare([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["0", "0", "1", "1", "1"]]) == 16
