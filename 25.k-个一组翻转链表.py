#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy

# @lc code=end
