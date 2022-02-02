#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(None)
        cur = pre
        while list1 and list2:
            if list1.val <= list2.val:
                nextnode = ListNode(list1.val)
                list1 = list1.next
            else:
                nextnode = ListNode(list2.val)
                list2 = list2.next
            cur.next = nextnode
            cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return pre.next

# @lc code=end
