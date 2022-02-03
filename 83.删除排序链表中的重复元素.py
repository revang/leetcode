#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# @lc code=end


def test():
    val = Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2))))
    assert is_equal_listnode(val, ListNode(1, ListNode(2)))

    val = Solution().deleteDuplicates(ListNode(1, ListNode(1)))
    assert is_equal_listnode(val, ListNode(1))
