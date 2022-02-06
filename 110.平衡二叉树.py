#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
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
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left)-self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right))+1

# @lc code=end


def test():
    root = init_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    assert Solution().isBalanced(root) == False

    root = init_tree([])
    assert Solution().isBalanced(root) == True
