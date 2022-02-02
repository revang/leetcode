#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#


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
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(None, head)
        cur = pre
        size = self.get_length(head)
        for _ in range(size-n):
            cur = cur.next
        cur.next = cur.next.next
        return pre.next

    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

# @lc code=end
