#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

from typing import List
from heapq import heapify, heappop


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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        items = []
        for node in lists:
            while node:
                items.append(node.val)
                node = node.next
        heapify(items)  # 构造一个最小堆
        dummy = ListNode(0)
        cur = dummy
        while items:
            nextnode = ListNode(heappop(items))
            cur.next = nextnode
            cur = cur.next
        return dummy.next

# @lc code=end


def test():
    lists = [init_listnode([1, 4, 5]), init_listnode([1, 3, 4]), init_listnode([2, 6])]
    ans = Solution().mergeKLists(lists)
    print_listnode(ans)
