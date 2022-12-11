#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def sum(root):
            if not root:
                return 0
            return root.val+sum(root.left)+sum(root.right)

        if not root:
            return 0
        return self.findTilt(root.left)+self.findTilt(root.right)+abs(sum(root.left)-sum(root.right))
# @lc code=end


def test():
    assert Solution().findTilt(create_tree([1, 2, 3])) == 1
    assert Solution().findTilt(create_tree([4, 2, 9, 3, 5, None, 7])) == 15
    assert Solution().findTilt(create_tree([1, 2, None, 3, 4])) == 10
