#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        s = deque()  # 使用栈
        s.append((root, False))
        while s:
            node, visited = s.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    s.append((node.right, False))
                    s.append((node.left, False))
                    s.append((node, True))
        return res

# @lc code=end
