#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

    def __repr__(self):
        return "<Node: {}>".format(self.val)


def init_tree(values):
    queue = deque()
    root = None

    if values:
        root = TreeNode(values[0])
        queue.append(root)

    index = 1
    while index < len(values):
        node = queue.popleft()

        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root

# @lc code=start


class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.ans

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        self.ans = max(self.ans, left+right)  # 每个结点都要去判断左子树+右子树的高度是否大于self.max，更新最大值
        return max(left, right)+1

# @lc code=end


def test():
    root = init_tree([1, 2, 3, 4, 5])
    assert Solution().diameterOfBinaryTree(root) == 3
