#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPath(root):
            if not root:
                return 0
            return max(
                maxPath(root.left)+root.val,
                maxPath(root.right)+root.val,
                root.val)

        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        if not root.left:
            return max(
                maxPath(root.right)+root.val,
                root.val,
                self.maxPathSum(root.right))
        if not root.right:
            return max(maxPath(root.left)+root.val,
                       root.val,
                       self.maxPathSum(root.left))
        return max(maxPath(root.left)+maxPath(root.right)+root.val,
                   maxPath(root.left)+root.val,
                   maxPath(root.right)+root.val,
                   root.val,
                   self.maxPathSum(root.left),
                   self.maxPathSum(root.right))

# @lc code=end


def test():
    assert Solution().maxPathSum(create_tree([1, 2, 3])) == 6
    assert Solution().maxPathSum(create_tree([-10, 9, 20, None, None, 15, 7])) == 42
    assert Solution().maxPathSum(create_tree([-3])) == -3
    assert Solution().maxPathSum(create_tree([2, -1])) == 2
    assert Solution().maxPathSum(create_tree([1, -2, 3])) == 4
    assert Solution().maxPathSum(create_tree([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6])) == 16
