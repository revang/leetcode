#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

# @lc code=end


def test():
    root = init_tree([1, 0, 2])
    ans = Solution().trimBST(root, 1, 2)
    print_tree(ans)
