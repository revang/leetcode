#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        max_vals = []
        cur_nodes = deque()
        cur_nodes.append(root)

        while cur_nodes:
            cur_vals = [cur.val for cur in cur_nodes]
            max_vals.append(max(cur_vals))

            next_nodes = deque()
            for cur in cur_nodes:
                if cur.left:
                    next_nodes.append(cur.left)
                if cur.right:
                    next_nodes.append(cur.right)
            cur_nodes = next_nodes

        return max_vals

# @lc code=end


def test():
    assert Solution().largestValues(create_tree([1, 3, 2, 5, 3, None, 9])) == [1, 3, 9]
    assert Solution().largestValues(create_tree([1, 2, 3])) == [1, 3]
