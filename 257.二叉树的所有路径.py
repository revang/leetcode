#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:  # BFS
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        all_paths = []
        cur_nodes = deque()
        cur_nodes.append((root, [root.val]))

        while cur_nodes:
            next_nodes = deque()
            for cur_node, cur_vals in cur_nodes:
                if not cur_node.left and not cur_node.right:
                    all_paths.append("->".join([str(cur_val) for cur_val in cur_vals]))

                if cur_node.left:
                    next_nodes.append((cur_node.left, cur_vals+[cur_node.left.val]))
                if cur_node.right:
                    next_nodes.append((cur_node.right, cur_vals+[cur_node.right.val]))
                cur_nodes = next_nodes
        return all_paths


# @lc code=end

def test():
    assert Solution().binaryTreePaths(create_tree([1, 2, 3, None, 5])) == ["1->3", "1->2->5"]
    assert Solution().binaryTreePaths(create_tree([1])) == ["1"]
