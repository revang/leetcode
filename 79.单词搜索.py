#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

from typing import List

# @lc code=start


class Solution:
    def __init__(self) -> None:
        self.find = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        self.board = board
        self.word = word
        self.size_row = len(board)
        self.size_column = len(board[0])
        self.visited = [[False]*self.size_column for _ in range(self.size_row)]
        for i in range(self.size_row):
            for j in range(self.size_column):
                self.backtrack(i, j, 0)
        return self.find

    def backtrack(self, i, j, pos):
        if i < 0 or j < 0 or i >= self.size_row or j >= self.size_column:
            return
        if self.board[i][j] != self.word[pos] or self.visited[i][j] or self.find:
            return
        if pos == len(self.word)-1:
            self.find = True
            return
        self.visited[i][j] = True  # 将当前位置置为已访问
        self.backtrack(i+1, j, pos+1)
        self.backtrack(i-1, j, pos+1)
        self.backtrack(i, j+1, pos+1)
        self.backtrack(i, j-1, pos+1)
        self.visited[i][j] = False  # 将当前位置置为未访问

# @lc code=end


def test():
    assert Solution().exist(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]], "ABCCED") == True
