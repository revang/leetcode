#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        all_vals = []
        cur_nodes = deque()
        cur_nodes.append((root, [root.val]))

        while cur_nodes:
            next_nodes = deque()
            for cur_node, cur_vals in cur_nodes:
                if not cur_node.left and not cur_node.right:
                    val = 0
                    for x in cur_vals:
                        val = val*10+x
                    all_vals.append(val)

                if cur_node.left:
                    next_nodes.append((cur_node.left, cur_vals+[cur_node.left.val]))
                if cur_node.right:
                    next_nodes.append((cur_node.right, cur_vals+[cur_node.right.val]))
            cur_nodes = next_nodes

        return sum(all_vals)

# @lc code=end


def test():
    assert Solution().sumNumbers(create_tree([1, 2, 3])) == 25
    assert Solution().sumNumbers(create_tree([4, 9, 0, 5, 1])) == 1026
