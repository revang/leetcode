#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start


class Solution:
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.max

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        self.max = max(self.max, left+right)  # 每个结点都要去判断左子树+右子树的高度是否大于self.max，更新最大值
        return max(left, right)+1
# @lc code=end
