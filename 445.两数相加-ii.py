#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        0

# @lc code=end
