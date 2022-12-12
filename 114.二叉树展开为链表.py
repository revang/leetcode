#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        vals = []
        stack = deque()
        stack.append((root, False))

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    vals.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
                    stack.append((cur, True))

        cur = root
        for i in range(1, len(vals)):
            cur.val = vals[i-1]
            cur.left = None
            cur.right = TreeNode(vals[i])
            cur = cur.right


# @lc code=end
