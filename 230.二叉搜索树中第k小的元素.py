#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        stack.append((root, False))

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    k -= 1
                    if k == 0:
                        return cur.val
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        return -1

# @lc code=end


def test():
    assert Solution().kthSmallest(create_tree([3, 1, 4, None, 2]), 1) == 1
    assert Solution().kthSmallest(create_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
