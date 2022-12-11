#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入二叉搜索树
#

from typing import List, Optional
from collections import deque, defaultdict
from leetcode_tool import *


# @lc code=start

class Solution:  # DFS+哈希表
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashmap = defaultdict(int)
        stack = deque()
        stack.append((root, False))

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    if k-cur.val in hashmap:
                        return True
                    hashmap[cur.val] += 1
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))
        return False


class Solution:  # BFS+哈希表
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashmap = defaultdict(int)
        cur_nodes = deque()
        cur_nodes.append(root)

        while cur_nodes:
            next_nodes = deque()
            for cur in cur_nodes:
                if k-cur.val in hashmap:
                    return True
                hashmap[cur.val] += 1

                if cur.left:
                    next_nodes.append(cur.left)
                if cur.right:
                    next_nodes.append(cur.right)
            cur_nodes = next_nodes
        return False


class Solution:  # DFS+双指针
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals = []
        stack = deque()
        stack.append((root, False))

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    vals.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        left, right = 0, len(vals)-1
        while left < right:
            if vals[left]+vals[right] == k:
                return True
            if vals[left]+vals[right] > k:
                right -= 1
                continue
            if vals[left]+vals[right] < k:
                left += 1
                continue
        return False
# @lc code=end


def test():
    assert Solution().findTarget(create_tree([5, 3, 6, 2, 4, None, 7]), 9) == True
    assert Solution().findTarget(create_tree([5, 3, 6, 2, 4, None, 7]), 28) == False
