#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:  # BFS
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        all_paths = []
        cur_nodes = deque()
        cur_nodes.append((root, [root.val]))

        while cur_nodes:
            next_nodes = deque()
            for cur_node, cur_vals in cur_nodes:
                if not cur_node.left and not cur_node.right and sum(cur_vals) == targetSum:
                    all_paths.append(cur_vals)

                if cur_node.left:
                    next_nodes.append((cur_node.left, cur_vals+[cur_node.left.val]))
                if cur_node.right:
                    next_nodes.append((cur_node.right, cur_vals+[cur_node.right.val]))
            cur_nodes = next_nodes

        return all_paths


# @lc code=end
def test():
    assert Solution().pathSum(create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]
