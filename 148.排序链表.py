#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_listnode(head):
    """ 打印单链表 """
    cur = head
    while cur:
        print("{}->".format(cur.val), end="")
        cur = cur.next
    print("None")


def is_equal_listnode(head1, head2):
    """ 比较两个单链表是否相等 """
    if not head1 and not head2:
        return True
    if not head1 or not head2:
        return False
    return head1.val == head2.val and is_equal_listnode(head1.next, head2.next)


# @lc code=start
# Definition for singly-linked list.

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        right_half = self.sortList(slow.next)
        slow.next = None
        left_half = self.sortList(head)
        return self.merge(left_half, right_half)

    def merge(self, head1, head2):
        dummy = ListNode(None)
        cur = dummy
        cur1, cur2 = head1, head2
        while cur1 or cur2:
            if not cur1:
                cur.next = cur2
                break
            if not cur2:
                cur.next = cur1
                break
            if cur1.val < cur2.val:
                cur.next = ListNode(cur1.val)
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = ListNode(cur2.val)
                cur = cur.next
                cur2 = cur2.next
        return dummy.next

# @lc code=end


def test():
    res = Solution().sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
    print_listnode(res)
