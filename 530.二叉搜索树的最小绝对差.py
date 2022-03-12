#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

from typing import Optional
from collections import deque
import sys


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
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = sys.maxsize
        last = ans
        stack = deque()
        stack.append((root, False))
        while stack:
            node, visited = stack.pop()
            if visited:
                ans = min(ans, abs(node.val-last))
                last = node.val
            else:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
        return ans

# @lc code=end


def test():
    root = init_tree([4, 2, 6, 1, 3])
    ans = Solution().getMinimumDifference(root)
    print(ans)
    assert ans == 1

    root = init_tree([1, 0, 48, None, None, 12, 49])
    ans = Solution().getMinimumDifference(root)
    print(ans)
    assert ans == 1
