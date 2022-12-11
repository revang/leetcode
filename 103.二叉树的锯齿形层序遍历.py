#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        all_vals = []
        cur_nodes = deque()
        cur_nodes.append(root)
        level = 1

        while cur_nodes:
            cur_vals = [cur.val for cur in cur_nodes]
            cur_vals = cur_vals if level % 2 == 1 else cur_vals[::-1]
            all_vals.append(cur_vals)
            next_nodes = deque()
            for cur in cur_nodes:
                if cur.left:
                    next_nodes.append(cur.left)
                if cur.right:
                    next_nodes.append(cur.right)
            cur_nodes = next_nodes
            level += 1
        return all_vals


# @lc code=end

def test():
    assert Solution().zigzagLevelOrder(Tree([3, 9, 20, None, None, 15, 7]).root) == [[3], [20, 9], [15, 7]]
    assert Solution().zigzagLevelOrder(Tree([1]).root) == [[1]]
    assert Solution().zigzagLevelOrder(Tree([]).root) == []
