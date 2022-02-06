#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def init_listnode(nums):
    """ 列表生成单链表 """
    if not nums:
        return
    dummy = ListNode(None)
    cur = dummy
    for i in range(len(nums)):
        next = ListNode(nums[i])
        cur.next = next
        cur = cur.next
    return dummy.next


def print_listnode(head):
    """ 打印单链表 """
    cur = head
    while cur:
        print("{}->".format(cur.val), end="")
        cur = cur.next
    print("None")

# @lc code=start


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        mid = self.middle(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)
        self.merge(l1, l2)

    def middle(self, head):
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        return pre

    def merge(self, l1, l2):
        # dummy = ListNode(0, l1)
        while l1 and l2:
            next1 = l1.next
            next2 = l2.next
            l1.next = l2
            l1 = next1
            l2.next = l1
            l2 = next2


# @lc code=end


def test():
    head = init_listnode([1, 2, 3, 4])
    print_listnode(head)
    Solution().reorderList(head)
    print_listnode(head)
