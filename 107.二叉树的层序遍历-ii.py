#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        all_vals = []
        cur_nodes = deque()
        cur_nodes.append(root)

        while cur_nodes:
            all_vals.append([cur.val for cur in cur_nodes])
            next_nodes = deque()
            for cur in cur_nodes:
                if cur.left:
                    next_nodes.append(cur.left)
                if cur.right:
                    next_nodes.append(cur.right)
            cur_nodes = next_nodes

        return all_vals[::-1]

# @lc code=end


def test():
    assert Solution().levelOrderBottom(Tree([3, 9, 20, None, None, 15, 7]).root) == [[15, 7], [9, 20], [3]]
    assert Solution().levelOrderBottom(Tree([1]).root) == [[1]]
    assert Solution().levelOrderBottom(Tree([]).root) == []
