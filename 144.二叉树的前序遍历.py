#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

from typing import Optional, List
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        stack = deque()
        stack.append((root, False))
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    ans.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return ans


# @lc code=end

def test():
    root = init_tree([1, None, 2, 3])
    ans = Solution().preorderTraversal(root)
    assert ans == [1, 2, 3]
