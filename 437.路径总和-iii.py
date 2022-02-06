#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
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
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root is None:
            return 0
        ans = self.rootSum(root, targetSum)
        ans += self.pathSum(root.left, targetSum)
        ans += self.pathSum(root.right, targetSum)
        return ans

    def pathSumStartWithRoot(self, root, targetSum):
        if root is None:
            return 0
        ans = 1 if root.val == targetSum else 0
        ans += self.pathSumStartWithRoot(root.left, targetSum-root.val)
        ans += self.pathSumStartWithRoot(root.right, targetSum-root.val)
        return ans


# @lc code=end


def test():
    root = init_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    assert Solution().pathSum(root, 8) == 3

    root = init_tree([1, None, 2, None, 3, None, 4, None, 5])
    assert Solution().pathSum(root, 3) == 2
