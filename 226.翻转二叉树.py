#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# @lc code=end


def test():
    assert is_same_tree(Solution().invertTree(Tree([4, 2, 7, 1, 3, 6, 9]).root), Tree([4, 7, 2, 9, 6, 3, 1]).root) == True
    assert is_same_tree(Solution().invertTree(Tree([2, 1, 3]).root), Tree([2, 3, 1]).root) == True
    assert is_same_tree(Solution().invertTree(Tree([]).root), Tree([]).root) == True
