#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = self.reverse_list(slow.next)
        slow = slow.next
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True

    def reverse_list(self, head):
        pre = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        return pre
# @lc code=end
