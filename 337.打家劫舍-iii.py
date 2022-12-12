#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        odd, even = 0, 0

        cur_nodes = deque()
        cur_nodes.append(root)
        idx = 1

        while cur_nodes:
            next_nodes = deque()
            for cur_node in cur_nodes:
                if cur_node:
                    if idx % 2 == 1:
                        odd += cur_node.val
                    else:
                        even += cur_node.val

                    if cur_node.left:
                        next_nodes.append(cur_node.left)
                    if cur_node.right:
                        next_nodes.append(cur_node.right)

            cur_nodes = next_nodes
            idx += 1

        return max(odd, even)

# @lc code=end


def test():
    assert Solution().rob(create_tree([3, 2, 3, None, 3, None, 1])) == 7
    assert Solution().rob(create_tree([3, 4, 5, 1, 3, None, 1])) == 9
    assert Solution().rob(create_tree([4, 1, None, 2, None, 3])) == 7
