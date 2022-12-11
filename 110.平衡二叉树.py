#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right))+1

        if not root:
            return True
        return abs(height(root.left)-height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# @lc code=end


def test():
    assert Solution().isBalanced(Tree([1, 2, 2, 3, 3, None, None, 4, 4]).root) == False
    assert Solution().isBalanced(Tree([]).root) == True
