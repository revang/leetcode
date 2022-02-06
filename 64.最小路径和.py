#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

from typing import List
# @lc code=start


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        size_row, size_column = len(grid), len(grid[0])
        dp = [[0]*size_column for _ in range(size_row)]
        for i in range(size_row):
            for j in range(size_column):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j])+grid[i][j]
        return dp[-1][-1]

# @lc code=end


def test():
    assert Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert Solution().minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
