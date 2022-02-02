#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

"""
author : revang
date   : 2022-02-02
method : 二叉树/递归
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return "{}({})".format(root.val, self.tree2str(root.left))
        return "{}({})({})".format(root.val, self.tree2str(root.left), self.tree2str(root.right))

# @lc code=end


def test():
    assert Solution().tree2str(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))) == "1(2(4))(3)"
