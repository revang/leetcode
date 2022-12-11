#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

import heapq
from typing import List, Optional
from collections import deque
from leetcode_tool import *


# @lc code=start


class Solution:  # 堆排序
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minheap = []
        heapq.heapify(minheap)

        stack = deque()
        stack.append((root, False))

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    if cur.val not in minheap:
                        heapq.heappush(minheap, cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        if len(minheap) < 2:
            return -1
        heapq.heappop(minheap)
        return heapq.heappop(minheap)


class Solution:  # DFS
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        """
        1. 二叉树根节点的值即为所有节点中的最小值。
        2. 对整棵二叉树进行一次遍历。设根节点的值为 rootvalue, 我们只需要通过遍历, 找出严格大于 rootvalue 的最小值, 即为「所有节点中的第二小的值」
        """
        ans, rootval = -1, root.val
        stack = deque()
        stack.append((root, False))

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    if cur.val > rootval and ans == -1:
                        ans = cur.val
                    if cur.val > rootval and cur.val < ans:
                        ans = cur.val
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))
        return ans

# @lc code=end


def test():
    assert Solution().findSecondMinimumValue(create_tree([2, 2, 5, None, None, 5, 7])) == 5
    assert Solution().findSecondMinimumValue(create_tree([2, 2, 2])) == -1
    assert Solution().findSecondMinimumValue(create_tree([5, 8, 5])) == 8
