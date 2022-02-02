#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None, head)
        pre = dummy  # pre 为需要交换节点的前一个节点
        while pre.next and pre.next.next:
            fst = pre.next
            sec = fst.next
            thr = sec.next
            pre.next = sec
            sec.next = fst
            fst.next = thr
            pre = pre.next.next
        return dummy.next

# @lc code=end
