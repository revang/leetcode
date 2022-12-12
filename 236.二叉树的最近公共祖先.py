#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None

# @lc code=end


# def test():
#     assert Solution().lowestCommonAncestor(create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 1) == 3
#     assert Solution().lowestCommonAncestor(create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 4) == 5
#     assert Solution().lowestCommonAncestor(create_tree([1, 2]), 1, 2) == 1
