#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

from typing import List

# @lc code=start

# 深度优先(递归)
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         max_area = 0
#         for i, l in enumerate(grid):
#             for j, m in enumerate(l):
#                 max_area = max(max_area, self.dfs(grid, i, j))
#         return max_area

#     def dfs(self, grid, cur_i, cur_j):
#         if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
#             return 0
#         area = 1
#         grid[cur_i][cur_j] = 0
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 以下(x)/右(y)为正方向建立坐标系: 右, 下, 左, 上
#         for direction in directions:
#             next_i = cur_i+direction[0]
#             next_j = cur_j+direction[1]
#             if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
#                 area += self.dfs(grid, next_i, next_j)
#         return area

from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i, l in enumerate(grid):
            for j, m in enumerate(l):
                cur_area = 0
                stack = deque()
                stack.append((i, j))
                while stack:
                    cur_i, cur_j = stack.pop()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    cur_area += 1
                    grid[cur_i][cur_j] = 0
                    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 以下(x)/右(y)为正方向建立坐标系: 右, 下, 左, 上
                    for direction in directions:
                        next_i = cur_i+direction[0]
                        next_j = cur_j+direction[1]
                        stack.append((next_i, next_j))
                max_area = max(max_area, cur_area)
        return max_area

# @lc code=end


def test():
    assert Solution().maxAreaOfIsland(
        [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6
