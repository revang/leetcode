#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque()
        stack.append((root, False))
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res

# @lc code=end


def test():
    assert Solution().inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None))) == [1, 3, 2]
    assert Solution().inorderTraversal(TreeNode(1)) == [1]
