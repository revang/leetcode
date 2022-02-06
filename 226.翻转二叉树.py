#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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


def print_tree(root):
    if not root:
        return
    cur_nodes = [root]
    while cur_nodes or next_nodes:
        print(cur_nodes)
        next_nodes = []
        for node in cur_nodes:
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)
        cur_nodes = next_nodes

# @lc code=start


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

# @lc code=end


def test():
    root = init_tree([2, 1, 3])
    ans = Solution().invertTree(root)
    print_tree(ans)
