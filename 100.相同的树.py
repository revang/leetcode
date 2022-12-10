#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

from typing import List, Optional
from leetcode_tool import *

# @lc code=start


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# @lc code=end


def test():
    assert Solution().isSameTree(Tree([1, 2, 3]).root, Tree([1, 2, 3]).root) == True
    assert Solution().isSameTree(Tree([1, 2]).root, Tree([1, None, 2]).root) == False
    assert Solution().isSameTree(Tree([1, 2, 1]).root, Tree([1, 1, 2]).root) == False
