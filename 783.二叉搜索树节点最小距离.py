#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start

"""
if not val 和 if val is None 的区别:
1. 如果 val 是 None, 两者都是True
2. 如果 val 是 0, if not val结果是True, if val is None结果是False

if not val, 对于 None, False, "", 0, [], {}, () 返回的都是True
"""


class Solution:  # DFS
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_val, pre_val = float("inf"), float("-inf")

        stack = deque()
        stack.append((root, False))

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    min_val = cur.val-pre_val if cur.val-pre_val < min_val else min_val
                    pre_val = cur.val
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        return min_val

# @lc code=end


def test():
    assert Solution().minDiffInBST(create_tree([4, 2, 6, 1, 3])) == 1
    assert Solution().minDiffInBST(create_tree([1, 0, 48, None, None, 12, 49])) == 1
    assert Solution().minDiffInBST(create_tree([5, 1, 7])) == 2
    assert Solution().minDiffInBST(create_tree([0, None, 2236, 1277, 2776, 519])) == 519
