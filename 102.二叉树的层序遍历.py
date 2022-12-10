#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return all_vals

# @lc code=end


def test():
    assert Solution().levelOrder(Tree([3, 9, 20, None, None, 15, 7]).root) == [[3], [9, 20], [15, 7]]
    assert Solution().levelOrder(Tree([1]).root) == [[1]]
    assert Solution().levelOrder(Tree([]).root) == []
