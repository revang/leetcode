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

    def merge(self, list1, list2):
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                cur = cur.next
                list2 = list2.next
        cur.next = list1 if list1 else list2
        return dummy.next

# @lc code=end


def test():
    print("demo 1")
    head = init_listnode([4, 2, 1, 3])
    print_listnode(head)
    ans = Solution().sortList(head)
    print_listnode(ans)

    print("demo 2")
    head = init_listnode([-1, 5, 3, 4, 0])
    print_listnode(head)
    ans = Solution().sortList(head)
    print_listnode(ans)
