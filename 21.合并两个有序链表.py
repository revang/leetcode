#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2


# 非递归
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(None)
#         cur = dummy
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 cur.next = ListNode(list1.val)
#                 cur = cur.next
#                 list1 = list1.next
#             else:
#                 cur.next = ListNode(list2.val)
#                 cur = cur.next
#                 list2 = list2.next
#         cur.next = list1 if list1 else list2
#         return dummy.next

# @lc code=end


def test():
    print("demo 1: ")
    l1 = init_listnode([1, 2, 4])
    l2 = init_listnode([1, 3, 4])
    print_listnode(l1)
    print_listnode(l2)
    ans = Solution().mergeTwoLists(l1, l2)
    print_listnode(ans)

    # print("demo 2: ")
    # l1 = init_listnode([])
    # l2 = init_listnode([])
    # print_listnode(l1)
    # print_listnode(l2)
    # ans = Solution().mergeTwoLists(l1, l2)
    # print_listnode(ans)

    # print("demo 3: ")
    # l1 = init_listnode([])
    # l2 = init_listnode([0])
    # print_listnode(l1)
    # print_listnode(l2)
    # ans = Solution().mergeTwoLists(l1, l2)
    # print_listnode(ans)
