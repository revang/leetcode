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
        dummy = ListNode(None)
        cur = dummy
        while list1 or list2:
            if not list1:
                cur.next = list2
                break
            if not list2:
                cur.next = list1
                break
            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                cur = cur.next
                list2 = list2.next
        return dummy.next

# @lc code=end
