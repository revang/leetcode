#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

"""
author : revang
date   : 2022-02-01
method : 链表
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        pre = ListNode(None)
        cur = pre
        while l1 or l2:
            sum = carry+(l1.val if l1 else 0)+(l2.val if l2 else 0)
            carry = sum//10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            cur.next = ListNode(carry)
        return pre.next

# @lc code=end


def testSolution():
    ans = Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
    assert is_equal_listnode(ans, ListNode(7, ListNode(0, ListNode(8))))

    ans = Solution().addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
    assert is_equal_listnode(ans, ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))))))
