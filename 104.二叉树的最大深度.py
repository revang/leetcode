#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *


# @lc code=start
# Definition for a binary tree node.


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

# @lc code=end


def test():
    assert Solution().maxDepth(Tree([3, 9, 20, None, None, 15, 7]).root) == 3
