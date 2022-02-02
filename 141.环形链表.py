#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

"""
author : revang
date   : 2022-02-02
method : 双指针-快慢指针
"""

from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

# @lc code=start


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

# @lc code=end
