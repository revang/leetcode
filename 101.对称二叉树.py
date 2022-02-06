#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.check(left.left, right.right) and self.check(left.right, right.left)

# @lc code=end


def test():
    root = init_tree([1, 2, 2, 3, 4, 4, 3])
    assert Solution().isSymmetric(root) == True

    root = init_tree([1, 2, 2, None, 3, None, 3])
    assert Solution().isSymmetric(root) == False
