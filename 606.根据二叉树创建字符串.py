#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *


# @lc code=start
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return "{}({})".format(root.val, self.tree2str(root.left))
        return "{}({})({})".format(root.val, self.tree2str(root.left), self.tree2str(root.right))

# @lc code=end


def test():
    assert Solution().tree2str(Tree([1, 2, 3, 4]).root) == "1(2(4))(3)"
    assert Solution().tree2str(Tree([1, 2, 3, None, 4]).root) == "1(2()(4))(3)"
