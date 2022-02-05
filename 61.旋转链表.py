#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

from typing import Optional


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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        size = self.listnode_length(head)
        right_count = size-k % size
        if size == right_count:
            return head

        cur = head
        while cur.next:
            cur = cur.next
        cur.next = head

        for _ in range(right_count):
            cur = cur.next
        ans = cur.next
        cur.next = None
        return ans

    def listnode_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length


# @lc code=end


def test():
    print("demo 1:")
    head = init_listnode([1, 2, 3, 4, 5])
    print_listnode(head)
    ans = Solution().rotateRight(head, 2)
    print_listnode(ans)

    print("demo 2:")
    head = init_listnode([0, 1, 2])
    print_listnode(head)
    ans = Solution().rotateRight(head, 4)
    print_listnode(ans)
