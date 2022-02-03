#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root.left, root.right)

    def dfs(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)

# @lc code=end
