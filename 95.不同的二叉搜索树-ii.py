#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#


from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTrees(left: int, right: int):
            if left > right:
                return [None]
            res = []
            for i in range(left, right+1):
                left_trees = generateTrees(left, i-1)
                right_trees = generateTrees(i+1, right)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        curr = TreeNode(i, left_tree, right_tree)
                        res.append(curr)
            return res

        return generateTrees(1, n) if n != 0 else []

# @lc code=end


def test():
    Solution().generateTrees(3)
