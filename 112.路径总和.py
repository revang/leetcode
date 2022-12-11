#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:  # BFS
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        cur_nodes = deque()
        cur_nodes.append((root, root.val))

        while cur_nodes:
            next_nodes = deque()
            for cur_node, cur_val in cur_nodes:
                if not cur_node.left and not cur_node.right and cur_val == targetSum:
                    return True

                if cur_node.left:
                    next_nodes.append((cur_node.left, cur_node.left.val+cur_val))
                if cur_node.right:
                    next_nodes.append((cur_node.right, cur_node.right.val+cur_val))
                cur_nodes = next_nodes

        return False

# @lc code=end


def test():
    assert Solution().hasPathSum(create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) == True
    assert Solution().hasPathSum(create_tree([1, 2, 3]), 5) == False
    assert Solution().hasPathSum(create_tree([]), 0) == False
