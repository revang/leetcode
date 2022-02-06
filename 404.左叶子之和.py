#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        self.dfs(root)
        return self.sum

    def dfs(self, root):
        if root is None:
            return
        if root.left and root.left.left is None and root.left.right is None:
            self.sum += root.left.val
        self.dfs(root.left)
        self.dfs(root.right)

# @lc code=end


def test():
    root = init_tree([3, 9, 20, None, None, 15, 7])
    ans = Solution().sumOfLeftLeaves(root)
    print(ans)
    assert ans == 24
