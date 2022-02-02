#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

"""
author : revang
date   : 2022-02-02
method : 双指针-快慢指针
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val, self.next = val, next


def is_equal_listnode(head1, head2):
    """ 比较两个单链表是否相等 """
    if not head1 and not head2:
        return True
    if not head1 or not head2:
        return False
    return head1.val == head2.val and is_equal_listnode(head1.next, head2.next)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow = head.next
        fast = head.next.next
        while slow != fast:
            if not fast or not fast.next:
                return
            slow = slow.next
            fast = fast.next.next
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
        # @lc code=end
