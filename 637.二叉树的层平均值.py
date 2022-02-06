#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        if root is None:
            return ans
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            count = len(queue)
            sum = 0
            for _ in range(count):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sum/count)
        return ans

# @lc code=end


def test():
    root = init_tree([3, 9, 20, None, None, 15, 7])
    assert Solution().averageOfLevels(root) == [3.0, 14.5, 11.0]
