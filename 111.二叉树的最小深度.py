#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
from collections import deque
from typing import Optional


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
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left or not root.right:
            return left+right+1
        else:
            return min(left, right)+1

# @lc code=end


def test():
    tree = init_tree([3, 9, 20, None, None, 15, 7])
    print_tree(tree)
    # assert Solution().minDepth(TreeNode(3, TreeNode,))
