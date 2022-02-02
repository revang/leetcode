#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        evenhead = head.next
        odd, even = head, evenhead
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
        return head

# @lc code=end


def test():
    val1 = Solution().oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    val2 = ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4)))))
    assert is_equal_listnode(val1, val2)
