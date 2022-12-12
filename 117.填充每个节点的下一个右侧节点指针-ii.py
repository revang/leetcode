#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# @lc code=start


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        cur_nodes = deque()
        cur_nodes.append(root)

        while cur_nodes:
            next_nodes = deque()
            for idx, cur in enumerate(cur_nodes):
                if idx == len(cur_nodes)-1:
                    cur.next = None
                else:
                    cur.next = cur_nodes[idx+1]

                if cur.left:
                    next_nodes.append(cur.left)
                if cur.right:
                    next_nodes.append(cur.right)
            cur_nodes = next_nodes

        return root

# @lc code=end
